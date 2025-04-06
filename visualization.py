import matplotlib.pyplot as plt
import pandas as pd

def display_traffic_summary(df):
    plt.figure(figsize=(8, 4))
    plt.bar(df['location_id'], df['traffic_volume'], color='lightblue')
    plt.title("Traffic Volume by Location")
    plt.xlabel("Location ID")
    plt.ylabel("Traffic Volume")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_congestion_pie(df):
    plt.figure(figsize=(5, 5))
    df['congestion_level'].value_counts().plot.pie(autopct='%1.1f%%', colors=['green', 'orange', 'red'])
    plt.title("Congestion Levels Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def plot_optimization_plan(plan):
    loc = [p['location_id'] for p in plan]
    speeds = [p['target_speed'] for p in plan]
    plt.figure(figsize=(8, 4))
    plt.bar(loc, speeds, color='cyan')
    plt.title("Optimized Target Speeds")
    plt.xlabel("Location ID")
    plt.ylabel("Target Speed (km/h)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_accident_timeline(incidents):
    if incidents.empty:
        print("No accidents to visualize.")
        return
    plt.figure(figsize=(10, 4))
    incidents['count'] = 1
    grouped = incidents.groupby('timestamp').count()['count']
    grouped.plot(marker='o', linestyle='-')
    plt.title("Accident Reports Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Number of Accidents")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def plot_prediction_bar(predictions):
    plt.figure(figsize=(8, 4))
    locs = list(predictions.keys())
    vols = list(predictions.values())
    plt.bar(locs, vols, color='teal')
    plt.title("Predicted Traffic Volume")
    plt.xlabel("Location ID")
    plt.ylabel("Predicted Volume")
    plt.tight_layout()
    plt.show()

def animate_traffic_volume(df):
    # Placeholder for animation code — can be added using matplotlib.animation
    pass

def plot_prediction_accuracy(df, predictions):
    df['hour'] = df['timestamp'].dt.hour
    actual = df.groupby('location_id')['traffic_volume'].mean()
    pred = pd.Series(predictions)
    
    comparison = pd.DataFrame({'Actual': actual, 'Predicted': pred})
    comparison.dropna(inplace=True)
    
    comparison.plot(kind='bar', figsize=(10, 5), colormap='viridis')
    plt.title("Actual vs Predicted Traffic Volume")
    plt.ylabel("Traffic Volume")
    plt.xlabel("Location ID")
    plt.tight_layout()
    plt.grid(True, axis='y')
    plt.show()
