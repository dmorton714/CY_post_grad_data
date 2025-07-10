import pandas as pd


def compute_summary_stats(df: pd.DataFrame) -> pd.Series:
    return df['trip_duration_minutes'].describe()
