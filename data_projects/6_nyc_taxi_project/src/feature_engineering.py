import pandas as pd


def add_trip_duration(df: pd.DataFrame) -> pd.DataFrame:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])
    calc = df['dropoff_datetime'] - df['pickup_datetime']
    df['trip_duration_minutes'] = calc.dt.total_seconds() / 60
    return df
