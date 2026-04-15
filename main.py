"""
main.py
Orchestrates the pairs trading workflow.
"""

from data import load_data
from spread import compute_spread, compute_zscore
from strategy import generate_signals, compute_performance
from visualization import plot_spread, plot_zscore, plot_3d_scatter


def main():
    """
    Main entry point for the pairs trading system.
    Generates synthetic data, computes spread/z-score, runs strategy, and plots graphs.
    """
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 500
    dates = pd.date_range('2022-01-01', periods=n)
    # Generate two correlated assets
    asset1 = np.cumsum(np.random.normal(0, 1, n)) + 100
    asset2 = asset1 + np.random.normal(0, 1, n) + 2
    df = pd.DataFrame({'date': dates, 'asset1': asset1, 'asset2': asset2})

    # Compute spread and z-score
    df['spread'] = compute_spread(df)
    df['zscore'] = compute_zscore(df['spread'])

    # Generate trading signals and performance
    signals = generate_signals(df['zscore'])
    df = pd.concat([df, signals], axis=1)
    perf = compute_performance(df)

    # Print trade log and performance summary
    print("Trade Log:")
    print(df[['date', 'signal', 'position', 'spread', 'zscore', 'profit']].dropna().head(10))
    print("\nPerformance Summary:")
    for k, v in perf.items():
        print(f"{k}: {v}")

    # Plot graphs
    plot_spread(df)
    plot_zscore(df)
    plot_3d_scatter(df)
    import matplotlib.pyplot as plt
    plt.show()


if __name__ == "__main__":
    main()
