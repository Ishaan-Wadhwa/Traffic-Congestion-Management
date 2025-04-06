def detect_accidents(df):
    incidents = df[df['accident_reported'] == 1]
    return incidents[['timestamp', 'location_id', 'avg_vehicle_speed', 'traffic_volume']]
