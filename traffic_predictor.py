import numpy as np

def predict_traffic(df):
    predictions = {}
    df['hour'] = df['timestamp'].dt.hour
    for loc in df['location_id'].unique():
        sub = df[df['location_id'] == loc]
        mean_volume = sub['traffic_volume'].tail(10).mean()
        predictions[loc] = round(mean_volume + np.random.normal(0, 3), 2)
        clean_predictions = {int(k): v for k, v in predictions.items()}
    return clean_predictions
