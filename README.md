# Plant Leaf Disease Detector

Transfer learning (MobileNetV2, PyTorch) on the PlantVillage dataset.

## 1. Setup
```bash
pip install -r requirements.txt
```

## 2. Get the data from Kaggle
Put your `kaggle.json` in `~/.kaggle/`, then:
```bash
kaggle datasets download -d abdallahalidev/plantvillage-dataset
unzip plantvillage-dataset.zip -d data
```
Use the `color` folder (one sub-folder per class), e.g. `data/plantvillage dataset/color`.

## 3. Train
```bash
python train.py --data_dir "data/plantvillage dataset/color" --epochs 5
```
Creates `model/model.pt` and `model/classes.json`. A GPU is strongly recommended
(Kaggle/Colab free GPU works fine; then download the `model/` folder).

## 4. Predict
```bash
python predict.py leaf.jpg   # command line
python app.py                # web app
```

## Notes
- PlantVillage photos have plain backgrounds, so accuracy on real field photos
  will be lower. Add your own field images as extra class folders to improve it.
- The model only knows the crops/diseases in the dataset (38 classes).
- Results now include About, Treatment and Prevention advice from `treatments.py` (edit it to customize for your region).

## Web app
Run `python app.py` and open http://localhost:5000. On a phone connected to the same Wi-Fi, open `http://<your-computer-ip>:5000`; the "Take photo" button opens the phone camera.
