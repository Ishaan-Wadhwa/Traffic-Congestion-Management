import streamlit as st
import pandas as pd

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
    plot_prediction_accuracy
)

st.set_page_config(layout="wide", page_title="Smart Traffic Management Dashboard")
st.title("🚦 Smart Traffic Management Dashboard")

uploaded_file = st.file_uploader("Upload traffic dataset (CSV)", type="csv")

if uploaded_file:
    df = load_traffic_data(uploaded_file)
    st.success("✅ Dataset Loaded")

    if st.checkbox("📊 Show Raw Data"):
        st.dataframe(df.head(100))

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Traffic Analysis",
        "Optimization Plan",
        "Incident Detection",
        "Traffic Prediction",
        "Model Comparison"
    ])

    with tab1:
        st.subheader("📈 Traffic Analysis")
        analysis = analyze_traffic(df)
        st.dataframe(analysis)
        display_traffic_summary(analysis)
        plot_congestion_pie(analysis)

    with tab2:
        st.subheader("🛠️ Optimization Plan")
        plan = optimize_traffic_flow(analysis)
        st.dataframe(plan)
        plot_optimization_plan(plan)

    with tab3:
        st.subheader("🚨 Incident Detection")
        incidents = detect_accidents(df)
        st.dataframe(incidents)
        plot_accident_timeline(incidents)

    with tab4:
        st.subheader("🔮 Traffic Prediction")
        predictions = predict_traffic(df)

        if isinstance(predictions, dict):
        # Convert prediction dict to DataFrame
            pred_df = pd.DataFrame(list(predictions.items()), columns=["Location ID", "Predicted Volume"])
            pred_df["Predicted Volume"] = pred_df["Predicted Volume"].astype(float)

        # Show Metrics for each location
            st.markdown("### 📍 Location-wise Predictions")
            cols = st.columns(len(pred_df))
            for i, row in pred_df.iterrows():
                cols[i].metric(label=f"Location {row['Location ID']}", value=f"{row['Predicted Volume']:.2f} vehicles")

        # Show a bar chart for the predictions
            st.markdown("### 📊 Predicted Traffic Volume")
            st.bar_chart(pred_df.set_index("Location ID"))

        else:
            st.warning("Prediction format is invalid.")

    # Existing visualizations
        plot_prediction_bar(predictions)
        plot_prediction_accuracy(df, predictions)

    with tab5:
        st.subheader("🤖 Model Comparison")
        import matplotlib.pyplot as plt

        results = compare_models(df)
        st.write("### 📊 Mean Squared Error of Models")
        st.json({str(k): float(v) for k, v in results.items()})  # Clean keys/values

# Plot
        fig, ax = plt.subplots()
        ax.bar(results.keys(), results.values(), color=["skyblue", "orange"])
        ax.set_title("Model Comparison (MSE)")
        ax.set_ylabel("Mean Squared Error")
        st.pyplot(fig)

