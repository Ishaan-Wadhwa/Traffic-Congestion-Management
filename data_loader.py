import pandas as pd

def load_traffic_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    df['avg_vehicle_speed'].fillna(df['avg_vehicle_speed'].mean(), inplace=True)
    df['traffic_volume'].fillna(0, inplace=True)
    return df
