import numpy as np
from PIL import Image
import os

try:
    import clip
    import torch

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)

    CLIP_AVAILABLE = True

except Exception as e:
    print("CLIP not available:", e)
    CLIP_AVAILABLE = False


def get_embedding(image_path):

    # -------------------------------
    # SAFE FALLBACK MODE
    # -------------------------------
    if not CLIP_AVAILABLE:
        # simple fallback feature (so app doesn't crash)
        img = Image.open(image_path).resize((32, 32)).convert("L")
        arr = np.array(img).flatten().astype(np.float32)
        arr = arr / (np.linalg.norm(arr) + 1e-9)
        return arr[:512]  # match size

    # -------------------------------
    # CLIP MODE
    # -------------------------------
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

    with torch.no_grad():
        embedding = model.encode_image(image)

    embedding = embedding / embedding.norm(dim=-1, keepdim=True)

    return embedding.cpu().numpy().flatten()