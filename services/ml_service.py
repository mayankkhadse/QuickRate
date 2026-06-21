import os
import pickle

MODEL_PATH = "ml/model.pkl"


def load_model():
    try:
        if not os.path.exists(MODEL_PATH):
            return None

        if os.path.getsize(MODEL_PATH) == 0:
            return None

        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)

    except Exception:
        return None


def predict_price(buy, qty, branch_code):
    model = load_model()

    # fallback if no trained model exists
    if model is None:
        return round(buy * 1.30, 2)

    prediction = model.predict([[buy, qty, branch_code]])

    return round(prediction[0], 2)