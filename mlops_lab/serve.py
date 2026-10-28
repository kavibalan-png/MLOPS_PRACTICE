from flask import Flask, request, jsonify
import joblib, numpy as np

app = Flask(__name__)
model = joblib.load("models/model.joblib")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/predict", methods=["POST"])
def predict():
    features = np.array(request.json["features"]).reshape(1, -1)
    return jsonify({"prediction": str(model.predict(features)[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
