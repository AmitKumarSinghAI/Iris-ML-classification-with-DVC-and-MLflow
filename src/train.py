import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import mlflow
import mlflow.sklearn


# Load data
df = pd.read_csv("data/iris.csv")

X = df.drop("target", axis=1)
y = df["target"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Parameters
n_estimators = 200
max_depth = 3


# Model
model = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=max_depth,
    random_state=42
)


# MLflow experiment


mlflow.set_experiment("Iris Classification")


with mlflow.start_run(run_name="5 run"):

    # Train
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Metric
    accuracy = accuracy_score(y_test, predictions)

    # Log parameters
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(
        model,
        "model"
    )

    print("Accuracy:", accuracy)