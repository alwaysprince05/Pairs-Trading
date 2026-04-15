"""
visualization.py
Plots spread, z-score, and 3D scatter with quant-style visuals.
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_spread(df: pd.DataFrame):
    """
    Plots the spread with a dark quant-style theme.
    """
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df['date'], df['spread'], color='#00FFAA', linewidth=2, label='Spread')
    ax.set_title('Spread (Asset1 - Asset2)', color='w')
    ax.set_xlabel('Date', color='w')
    ax.set_ylabel('Spread', color='w')
    ax.grid(alpha=0.2)
    ax.legend()
    plt.tight_layout()
    # plt.show() removed to allow batch display


def plot_zscore(df: pd.DataFrame):
    """
    Plots the z-score with thresholds highlighted.
    """
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df['date'], df['zscore'], color='#FFCC00', linewidth=2, label='Z-Score')
    ax.axhline(2, color='#FF3366', linestyle='--', linewidth=1, label='Upper Threshold')
    ax.axhline(-2, color='#33CCFF', linestyle='--', linewidth=1, label='Lower Threshold')
    ax.axhline(0, color='w', linestyle=':', linewidth=1, label='Zero')
    ax.set_title('Spread Z-Score', color='w')
    ax.set_xlabel('Date', color='w')
    ax.set_ylabel('Z-Score', color='w')
    ax.grid(alpha=0.2)
    ax.legend()
    plt.tight_layout()
    # plt.show() removed to allow batch display


def plot_3d_scatter(df: pd.DataFrame):
    """
    Plots a 3D scatter: X=spread, Y=z-score, Z=profit, with gradient colors.
    """
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    x = df['spread']
    y = df['zscore']
    z = df['profit'].cumsum()
    norm = plt.Normalize(z.min(), z.max())
    colors = plt.cm.plasma(norm(z))
    ax.scatter(x, y, z, c=colors, marker='o', s=10, alpha=0.8)
    ax.set_xlabel('Spread', color='w')
    ax.set_ylabel('Z-Score', color='w')
    ax.set_zlabel('Cumulative Profit', color='w')
    ax.set_title('3D Scatter: Spread, Z-Score, Profit', color='w')
    plt.tight_layout()
    # plt.show() removed to allow batch display
