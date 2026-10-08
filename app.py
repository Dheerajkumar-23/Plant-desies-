"""Leaf disease web app.

Run:  python app.py
Open: http://localhost:5000  (on a phone on the same Wi-Fi: http://<your-pc-ip>:5000)
"""
from flask import Flask, jsonify, request, send_from_directory
from PIL import Image, UnidentifiedImageError
from pathlib import Path

from predict import load_model, predict
from treatments import DISCLAIMER, get_advice

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=str(BASE_DIR / "static"))
app.config["MAX_CONTENT_LENGTH"] = 15 * 1024 * 1024  # 15 MB

model, classes = load_model()


def split_name(raw):
    crop, _, disease = raw.partition("___")
    clean = lambda s: s.replace("_", " ").strip()
    return clean(crop), clean(disease)


@app.get("/")
def index():
    return send_from_directory(str(BASE_DIR / "static"), "index.html")


@app.post("/predict")
def predict_route():
    file = request.files.get("image")
    if not file:
        return jsonify(error="No image received. Choose a photo and try again."), 400
    try:
        img = Image.open(file.stream)
        img.load()
    except (UnidentifiedImageError, OSError):
        return jsonify(error="That file is not a readable image. Use a JPG or PNG photo."), 400

    try:
        results = predict(img, model, classes, top_k=3)
        _, conf, raw = results[0]
        crop, disease = split_name(raw)
        info = get_advice(raw)

        others = []
        for _, c, r in results[1:]:
            oc, od = split_name(r)
            others.append({"crop": oc, "disease": od, "confidence": c})

        return jsonify(
            crop=crop,
            disease=disease,
            healthy="healthy" in disease.lower(),
            confidence=conf,
            about=info["about"],
            treatment=info["treatment"],
            prevention=info["prevention"],
            others=others,
            disclaimer=DISCLAIMER,
        )
    except Exception as exc:
        app.logger.exception("Prediction failed")
        return jsonify(error=f"Prediction failed: {exc}"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
