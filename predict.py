"""Predict a leaf disease from an image.

Usage:
    python predict.py leaf.jpg
"""
import json, sys
from pathlib import Path

import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms

MODEL_DIR = Path(__file__).parent / "model"
TF = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])


def load_model(model_dir=MODEL_DIR):
    classes = json.loads((Path(model_dir) / "classes.json").read_text())
    model = models.mobilenet_v2()
    model.classifier[1] = nn.Linear(model.last_channel, len(classes))
    model.load_state_dict(torch.load(Path(model_dir) / "model.pt", map_location="cpu"))
    model.eval()
    return model, classes


def predict(image, model, classes, top_k=3):
    x = TF(image.convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        probs = torch.softmax(model(x), dim=1)[0]
    conf, idx = probs.topk(top_k)
    return [(classes[i].replace("___", " - ").replace("_", " "), c.item(), classes[i])
            for c, i in zip(conf, idx)]


if __name__ == "__main__":
    model, classes = load_model()
    from treatments import get_advice, DISCLAIMER
    results = predict(Image.open(sys.argv[1]), model, classes)
    for label, c, _ in results:
        print(f"{label}: {c:.1%}")
    info = get_advice(results[0][2])
    print("\nAbout:", info["about"])
    print("\nTreatment:")
    for t in info["treatment"]:
        print(" -", t)
    print("\nPrevention:")
    for t in info["prevention"]:
        print(" -", t)
    print("\n" + DISCLAIMER)
