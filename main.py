from data_loader import load_traffic_data
from traffic_analyzer import analyze_traffic
from traffic_optimizer import optimize_traffic_flow
from incident_detector import detect_accidents
from traffic_predictor import predict_traffic
from model_comparison import compare_models
from visualization import (
    display_traffic_summary,
    plot_congestion_pie,
    plot_optimization_plan,
    plot_accident_timeline,
    plot_prediction_bar,
    animate_traffic_volume,
    plot_prediction_accuracy
)

def main():
    traffic_data = load_traffic_data("./smart_traffic_management_dataset.csv")
    print("Loaded Traffic Data:\n", traffic_data.head(), "\n")

    traffic_analysis = analyze_traffic(traffic_data)
    print("Traffic Analysis Summary:\n", traffic_analysis, "\n")

    optimization_plan = optimize_traffic_flow(traffic_analysis)
    print("Traffic Signal Optimization Plan:\n", optimization_plan, "\n")

    incidents = detect_accidents(traffic_data)
    print("Detected Accidents:\n", incidents, "\n")

    predictions = predict_traffic(traffic_data)
    print("Predicted Traffic Volumes:\n", predictions, "\n")

    compare_models(traffic_data)

    # Visualizations
    display_traffic_summary(traffic_analysis)
    plot_congestion_pie(traffic_analysis)
    plot_optimization_plan(optimization_plan)
    plot_accident_timeline(incidents)
    plot_prediction_bar(predictions)
    # animate_traffic_volume(traffic_data)
    plot_prediction_accuracy(traffic_data, predictions)

if __name__ == "__main__":
    main()
