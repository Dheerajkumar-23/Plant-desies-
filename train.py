"""Train a leaf disease classifier on the PlantVillage dataset.

Usage:
    python train.py --data_dir path/to/plantvillage/color --epochs 5
"""
import argparse, json, time
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, models, transforms

MEAN, STD = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]


def get_device():
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data_dir", required=True, help="Folder with one sub-folder per class")
    p.add_argument("--epochs", type=int, default=5)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--lr", type=float, default=3e-4)
    p.add_argument("--val_split", type=float, default=0.2)
    p.add_argument("--out_dir", default="model")
    a = p.parse_args()

    train_tf = transforms.Compose([
        transforms.RandomResizedCrop(224, scale=(0.7, 1.0)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.ColorJitter(0.2, 0.2, 0.2),
        transforms.ToTensor(),
        transforms.Normalize(MEAN, STD),
    ])
    val_tf = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(MEAN, STD),
    ])

    # Two views of the same folder so train/val get different transforms
    train_full = datasets.ImageFolder(a.data_dir, transform=train_tf)
    val_full = datasets.ImageFolder(a.data_dir, transform=val_tf)
    classes = train_full.classes
    print(f"{len(train_full)} images, {len(classes)} classes")

    g = torch.Generator().manual_seed(42)
    perm = torch.randperm(len(train_full), generator=g).tolist()
    n_val = int(len(perm) * a.val_split)
    train_ds = Subset(train_full, perm[n_val:])
    val_ds = Subset(val_full, perm[:n_val])

    train_dl = DataLoader(train_ds, a.batch_size, shuffle=True, num_workers=2)
    val_dl = DataLoader(val_ds, a.batch_size, num_workers=2)

    device = get_device()
    print("Device:", device)

    model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    model.classifier[1] = nn.Linear(model.last_channel, len(classes))
    model.to(device)

    loss_fn = nn.CrossEntropyLoss()
    opt = torch.optim.AdamW(model.parameters(), lr=a.lr)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=a.epochs)

    out = Path(a.out_dir)
    out.mkdir(exist_ok=True)
    (out / "classes.json").write_text(json.dumps(classes, indent=2))

    best = 0.0
    for epoch in range(1, a.epochs + 1):
        t0 = time.time()
        model.train()
        total_loss = 0.0
        for x, y in train_dl:
            x, y = x.to(device), y.to(device)
            opt.zero_grad()
            loss = loss_fn(model(x), y)
            loss.backward()
            opt.step()
            total_loss += loss.item() * x.size(0)
        sched.step()

        model.eval()
        correct = 0
        with torch.no_grad():
            for x, y in val_dl:
                x, y = x.to(device), y.to(device)
                correct += (model(x).argmax(1) == y).sum().item()
        acc = correct / len(val_ds)
        print(f"Epoch {epoch}/{a.epochs}  loss={total_loss/len(train_ds):.4f}  "
              f"val_acc={acc:.4f}  ({time.time()-t0:.0f}s)")

        if acc > best:
            best = acc
            torch.save(model.state_dict(), out / "model.pt")
            print("  saved best model")

    print(f"Done. Best val accuracy: {best:.4f}")


if __name__ == "__main__":
    main()
