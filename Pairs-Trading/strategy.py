"""
strategy.py
Implements trading logic and performance metrics.
"""


import pandas as pd
import numpy as np


def generate_signals(zscore: pd.Series) -> pd.DataFrame:
    """
    Generates trading signals based on z-score thresholds.
    Returns DataFrame with signals, positions, and profit.
    """
    signals = pd.DataFrame(index=zscore.index)
    signals['signal'] = 0
    signals.loc[zscore > 2, 'signal'] = -1  # Short spread
    signals.loc[zscore < -2, 'signal'] = 1  # Long spread
    # Forward fill position
    signals['position'] = signals['signal'].replace(0, np.nan).ffill().fillna(0)
    # Exit when z-score crosses zero
    signals.loc[(signals['position'] == 1) & (zscore > -0.1) & (zscore < 0.1), 'position'] = 0
    signals.loc[(signals['position'] == -1) & (zscore > -0.1) & (zscore < 0.1), 'position'] = 0
    signals['position'] = signals['position'].replace(0, np.nan).ffill().fillna(0)
    # Calculate profit: position * spread change
    signals['profit'] = signals['position'].shift(1, fill_value=0) * (zscore - zscore.shift(1, fill_value=0))
    return signals


def compute_performance(df: pd.DataFrame) -> dict:
    """
    Computes total return, number of trades, and Sharpe ratio.
    """
    total_return = df['profit'].sum()
    num_trades = ((df['signal'].diff().abs() > 0) & (df['signal'] != 0)).sum()
    sharpe = df['profit'].mean() / (df['profit'].std(ddof=0) + 1e-8) * (252 ** 0.5)
    return {
        'Total Return': round(total_return, 4),
        'Number of Trades': int(num_trades),
        'Sharpe Ratio': round(sharpe, 4)
    }
