def optimize_traffic_flow(analysis):
    plan = []
    for _, row in analysis.iterrows():
        action = "Normal"
        if row['congestion_level'] == 'High':
            action = "Extend green"
        elif row['congestion_level'] == 'Low':
            action = "Shorten green"

        plan.append({
            'location_id': row['location_id'],
            'action': action,
            'target_speed': max(30, row['avg_vehicle_speed'] + 5)
        })
    return plan
