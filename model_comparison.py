import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

def custom_predictor(df):
    df['hour'] = df['timestamp'].dt.hour
    pred = []
    for _, row in df.iterrows():
        subset = df[(df['location_id'] == row['location_id']) & (df['hour'] == row['hour'])]
        est = subset['traffic_volume'].mean() + np.random.normal(0, 3)
        pred.append(est)
    return pred

def compare_models(df):
    print("\n--- Model Comparison ---")
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.dayofweek

    features = df[['location_id', 'hour', 'day']]
    target = df['traffic_volume']

    X = pd.get_dummies(features, columns=['location_id'])
    y = target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42, verbosity=0),
        "SVR": SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        results[name] = mse
        print(f"{name} MSE: {mse:.2f}")

    plt.figure(figsize=(10, 6))
    plt.bar(results.keys(), results.values(), color=['skyblue', 'orange', 'limegreen', 'violet'])
    plt.title("Model Comparison (MSE)")
    plt.ylabel("Mean Squared Error")
    plt.xticks(rotation=15)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return results
    
