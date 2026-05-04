from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(
    __file__), '', 'rf_model.pkl')
model = joblib.load(MODEL_PATH)
print(f"Model loaded from {MODEL_PATH}")

FEATURES = [
    'Account Balance', 'Duration of Credit (month)', 'Value Savings/Stocks', 'Credit Amount'
]


@app.route('/', methods=['GET'])
def home():
    """Home endpoint - tampilkan info API"""
    return jsonify({
        "message": "German Credit Random Forest API",
        "version": "1.0",
        "endpoints": {
            "/predict": "POST - Prediksi satu record",
            "/predict_batch": "POST - Prediksi banyak record (JSON array)",
            "/health": "GET - Cek status API"
        },
        "model": "Random Forest (tuned)",
        "features_count": len(FEATURES)
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None
    })


@app.route('/predict', methods=['POST'])
def predict():
    """Prediksi satu record kredit"""
    try:
        data = request.get_json()

        # Validasi input
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Extract features in correct order
        features = []
        for feat in FEATURES:
            if feat in data:
                features.append(data[feat])
            else:
                return jsonify({"error": f"Missing feature: {feat}"}), 400

        # Convert to numpy array and reshape
        X = np.array(features).reshape(1, -1)

        # Predict
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0].tolist()

        # Interpret prediction
        result = "Good" if prediction == 1 else "Bad"

        return jsonify({
            "prediction": int(prediction),
            "prediction_label": result,
            "probability_good": probability[1],
            "probability_bad": probability[0],
            "features_received": len(features)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    """Prediksi banyak record sekaligus"""
    try:
        data = request.get_json()

        if not isinstance(data, list):
            return jsonify({"error": "Input must be a JSON array"}), 400

        results = []
        for i, record in enumerate(data):
            features = []
            for feat in FEATURES:
                if feat in record:
                    features.append(record[feat])
                else:
                    return jsonify({"error": f"Record {i}: Missing feature: {feat}"}), 400

            X = np.array(features).reshape(1, -1)
            prediction = model.predict(X)[0]
            probability = model.predict_proba(X)[0].tolist()

            results.append({
                "record_id": i,
                "prediction": int(prediction),
                "prediction_label": "Good" if prediction == 1 else "Bad",
                "probability_good": probability[1],
                "probability_bad": probability[0]
            })

        # Summary
        good_count = sum(1 for r in results if r['prediction'] == 1)
        bad_count = len(results) - good_count

        return jsonify({
            "total_records": len(results),
            "predicted_good": good_count,
            "predicted_bad": bad_count,
            "results": results
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/model_info', methods=['GET'])
def model_info():
    """Informasi tentang model"""
    return jsonify({
        "model_type": "Random Forest Classifier",
        "features": FEATURES,
        "features_count": len(FEATURES),
        "target_classes": {
            "0": "Bad Credit",
            "1": "Good Credit"
        }
    })


if __name__ == '__main__':
    # Pastikan folder models ada
    models_dir = os.path.join(os.path.dirname(__file__), '')
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
        print(f"Created models directory: {models_dir}")
        print(
            f"Please copy your model file to: {os.path.join(models_dir, 'rf_model.pkl')}")

    app.run(debug=True, host='0.0.0.0', port=8080)
