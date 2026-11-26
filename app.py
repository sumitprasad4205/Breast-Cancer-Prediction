
from flask import Flask, render_template, request
import numpy as np
import joblib
import tensorflow as tf
from sklearn.datasets import load_breast_cancer

app = Flask(__name__)

# Load trained ANN model and scaler
model = tf.keras.models.load_model("model.keras")
scaler = joblib.load("scaler.pkl")

# Load dataset feature names in their original order
data = load_breast_cancer()
feature_names = data.feature_names.tolist()


@app.route("/")
def home():
    return render_template(
        "index.html",
        features=feature_names
    )


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Collect all 30 input features
        input_data = [
            float(request.form[f"feature_{i}"])
            for i in range(30)
        ]

        # Convert input into NumPy array
        input_array = np.array(input_data).reshape(1, -1)

        # Apply the same preprocessing used during training
        scaled_data = scaler.transform(input_array)

        # Make prediction using ANN
        prediction = model.predict(
            scaled_data, verbose=0
        )[0][0]

        # Assumes original sklearn target encoding:
        # 0 = Malignant, 1 = Benign
        if prediction >= 0.5:
            result = "Benign"
        else:
            result = "Malignant"

        return render_template(
            "index.html",
            features=feature_names,
            prediction=result,
            probability=round(float(prediction) * 100, 2)
        )

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            features=feature_names,
            error="Please enter valid numerical values for all 30 features."
        )


if __name__ == "__main__":
    app.run(debug=True)
