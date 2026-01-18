def sharpe_ratio(returns, freq=75):
    return np.sqrt(freq) * returns.mean() / returns.std()

def sortino_ratio(returns, freq=75):
    downside = returns[returns < 0]
    return np.sqrt(freq) * returns.mean() / downside.std()

def max_drawdown(cum_returns):
    peak = cum_returns.cummax()
    dd = (cum_returns - peak) / peak
    return dd.min()

def calmar_ratio(cum_returns, returns):
    total_return = cum_returns.iloc[-1] - 1
    mdd = abs(max_drawdown(cum_returns))
    return total_return / mdd if mdd != 0 else np.nan

def extract_trades(df):
    trades = []
    entry_time = None
    entry_price = None
    direction = None

    for i in range(1, len(df)):
        if df["position"].iloc[i] != df["position"].iloc[i-1]:
            # Entry
            if df["position"].iloc[i] != 0:
                entry_time = df["timestamp"].iloc[i]
                entry_price = df["open"].iloc[i]
                direction = df["position"].iloc[i]

            # Exit
            elif df["position"].iloc[i-1] != 0:
                exit_time = df["timestamp"].iloc[i]
                exit_price = df["open"].iloc[i]

                pnl = (
                    (exit_price - entry_price) / entry_price
                    if direction == 1
                    else (entry_price - exit_price) / entry_price
                )

                trades.append({
                    "entry_time": entry_time,
                    "exit_time": exit_time,
                    "pnl": pnl,
                    "duration": (exit_time - entry_time).seconds / 300
                })

    return pd.DataFrame(trades)

def backtest_metrics(df):
    returns = df["strategy_returns"].dropna()
    cum_returns = (1 + returns).cumprod()

    trades = extract_trades(df)

    metrics = {
        "Total Return": cum_returns.iloc[-1] - 1,
        "Sharpe Ratio": sharpe_ratio(returns),
        "Sortino Ratio": sortino_ratio(returns),
        "Calmar Ratio": calmar_ratio(cum_returns, returns),
        "Max Drawdown": max_drawdown(cum_returns),
        "Win Rate": (trades["pnl"] > 0).mean() if len(trades) > 0 else 0,
        "Profit Factor": (
            trades[trades["pnl"] > 0]["pnl"].sum() /
            abs(trades[trades["pnl"] < 0]["pnl"].sum())
            if len(trades[trades["pnl"] < 0]) > 0 else np.nan
        ),
        "Average Trade Duration (candles)": trades["duration"].mean() if len(trades) > 0 else 0,
        "Total Trades": len(trades)
    }

    return pd.Series(metrics)

