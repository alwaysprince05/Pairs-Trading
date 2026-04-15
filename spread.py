"""
spread.py
Calculates spread and z-score between two assets.
"""

import pandas as pd
import numpy as np


def compute_spread(df: pd.DataFrame) -> pd.Series:
    """
    Computes the spread between asset1 and asset2.
    """
    return df['asset1'] - df['asset2']


def compute_zscore(spread: pd.Series, window: int = 30) -> pd.Series:
    """
    Computes rolling z-score of the spread.
    """
    mean = spread.rolling(window=window, min_periods=1).mean()
    std = spread.rolling(window=window, min_periods=1).std(ddof=0)
    zscore = (spread - mean) / std
    return zscore
