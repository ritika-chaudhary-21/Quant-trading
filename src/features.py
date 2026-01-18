def compute_iv_ce(row):
    try:
        return implied_volatility(
            price=row["close_ce"],
            S=row["close_fut"],
            K=row["strike"],
            r=0.065,
            t=row["time_to_expiry"],
            flag="c"
        )
    except:
        return np.nan

def compute_iv_pe(row):
    try:
        return implied_volatility(
            price=row["close_pe"],
            S=row["close_fut"],
            K=row["strike_pe"],
            r=0.065,
            t=row["time_to_expiry"],
            flag="p"
        )
    except:
        return np.nan

