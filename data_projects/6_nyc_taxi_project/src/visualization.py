import pandas as pd
import matplotlib.pyplot as plt


def plot_trip_duration_histogram(df: pd.DataFrame, bins: int = 50) -> None:
    plt.figure(figsize=(8, 5))
    df['trip_duration_minutes'].hist(bins=bins)
    plt.xlabel('Trip Duration (minutes)')
    plt.ylabel('Frequency')
    plt.title('Histogram of NYC Taxi Trip Durations')
    plt.show()
