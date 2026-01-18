tscv = TimeSeriesSplit(n_splits=3)

xgb_model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=42
)

auc_scores = []

for fold, (train_idx, val_idx) in enumerate(tscv.split(X)):
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

    xgb_model.fit(X_train, y_train)
    probs = xgb_model.predict_proba(X_val)[:, 1]

    auc = roc_auc_score(y_val, probs)
    auc_scores.append(auc)

    print(f"Fold {fold} AUC: {auc:.4f}")
    
def make_lstm_sequences(X, y, seq_len):
    X_seq, y_seq = [], []

    for i in range(seq_len, len(X)):
        X_seq.append(X[i-seq_len:i])
        y_seq.append(y[i])

    return np.array(X_seq), np.array(y_seq)

def compute_metrics(df, pnl_col="pnl"):
    total_trades = len(df)
    win_rate = (df[pnl_col] > 0).mean() * 100
    total_pnl = df[pnl_col].sum()
    avg_pnl = df[pnl_col].mean()
    
    cum_pnl = df[pnl_col].cumsum()
    running_max = cum_pnl.cummax()
    drawdown = cum_pnl - running_max
    max_dd = drawdown.min()
    
    sharpe = (
        df[pnl_col].mean() / df[pnl_col].std()
        if df[pnl_col].std() != 0 else 0
    )
    
    return {
        "Total Trades": total_trades,
        "Win Rate (%)": round(win_rate, 2),
        "Total PnL": round(total_pnl, 2),
        "Avg PnL / Trade": round(avg_pnl, 2),
        "Max Drawdown": round(max_dd, 2),
        "Sharpe Ratio": round(sharpe, 2)
    }