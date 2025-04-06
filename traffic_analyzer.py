def analyze_traffic(df):
    grouped = df.groupby('location_id').agg({
        'traffic_volume': 'sum',
        'avg_vehicle_speed': 'mean'
    }).reset_index()

    def congestion_level(volume):
        if volume > 800:
            return 'High'
        elif volume > 400:
            return 'Medium'
        return 'Low'

    grouped['congestion_level'] = grouped['traffic_volume'].apply(congestion_level)
    grouped['avg_vehicle_speed'] = grouped['avg_vehicle_speed'].round(2)
    return grouped
