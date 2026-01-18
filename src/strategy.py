def strategy_metrics(trades, name):
    total_return = trades["pnl"].sum()
    win_rate = (trades["pnl"] > 0).mean()
    profit_factor = (
        trades.loc[trades["pnl"] > 0, "pnl"].sum() /
        abs(trades.loc[trades["pnl"] < 0, "pnl"].sum())
    )

    return {
        "Strategy": name,
        "Trades": len(trades),
        "Total Return": total_return,
        "Win Rate": win_rate,
        "Profit Factor": profit_factor
    }