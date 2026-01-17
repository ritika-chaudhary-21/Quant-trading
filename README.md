# ML-Enhanced Options Trading Strategy (NIFTY 5-Min Data)

## Project Overview
This project builds a quantitative options trading framework enhanced with machine learning.
A rule-based baseline strategy is first developed using technical indicators, options Greeks,
implied volatility, and market regime detection. Two machine learning models (XGBoost and LSTM)
are then used to filter trades and improve performance.

The goal is to evaluate whether ML-based trade filtering improves risk-adjusted returns
compared to a purely rule-based strategy.

---

## Key Objectives
- Engineer advanced features from futures & options data
- Detect market regimes
- Build a baseline trading strategy
- Train ML models to predict trade profitability
- Backtest and compare Baseline vs ML-enhanced strategies
- Analyze high-performance (outlier) trades

---

## Installation Instructions

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1: Feature Engineering
Generate engineered features and regime labels:
- nifty_features_5min.csv
- nifty_features_with_regime_5min.csv

### Step 2: Baseline Strategy
Run the baseline strategy and backtest:
- Generates nifty_baseline_strategy_5min.csv
- Outputs baseline performance metrics

### Step 3: Machine Learning Models
- Train XGBoost using time-series cross-validation
- Train LSTM using sequences of last 10 candles
- Generate prediction probabilities for each trade

### Step 4: ML-Enhanced Backtest
- Apply ML filter: take trades only when predicted probability > 0.5
- Compare Baseline vs XGBoost vs LSTM strategies

### Step 5: High-Performance Trade Analysis
- Identify outlier profitable trades
- Analyze IV, Greeks, regime, and time-of-day patterns

---

## Project Structure

```
├── data/
│   ├── nifty_features_5min.csv
│   ├── nifty_features_with_regime_5min.csv
│   ├── nifty_baseline_strategy_5min.csv
│   ├── nifty_strategy_results.csv
│
├── notebooks/
│   ├── 1_data_preparation.ipynb
│   ├── 2_feature_engineering.ipynb
│   ├── 3_strategy_backtest.ipynb
│   ├── 4_ml_models.ipynb
│   ├── 7_outlier_analysis.ipynb
│
├── src/
│   ├── data_utils.py
│   ├── features.py
│   ├── greeks.py
│   ├── regime.py
│   ├── strategy.py
│   ├── backtest.py
│   ├── ml_models.py
│
├── requirements.txt
├── README.md
```

---

## Key Results Summary

### Baseline Strategy
- Rule-based entries using EMA, IV, PCR, and regime filters
- Moderate win rate with stable trade frequency

### XGBoost Model
- Time-series cross-validation
- Improved trade selectivity
- Reduced number of low-quality trades
- Better risk-adjusted returns than baseline

### LSTM Model
- Sequential learning over last 10 candles
- Captures short-term temporal patterns
- More conservative trade filtering
- Lower variance performance

### High-Performance Trade Insights
- Extreme outliers were rare
- Profitable trades concentrated in specific regimes
- IV and Greeks were strong differentiators
- Best trades occurred during low-noise market periods

---

## Conclusion
Machine learning models improved the robustness of the trading strategy,
with XGBoost providing the strongest improvement in trade quality.
The framework is modular and extendable to other assets and models.

