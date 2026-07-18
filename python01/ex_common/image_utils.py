from __future__ import annotations
from typing import Tuple
import os
from PIL import Image, ImageDraw
import numpy as np

def ensure_sample(name: str, size: Tuple[int,int]=(256,256)) -> str:
    """Ensure an image file with `name` exists in the same folder and return its path."""
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, name)
    if os.path.exists(path):
        return path
    img = Image.new('RGB', size, color=(120,110,130))
    draw = ImageDraw.Draw(img)
    # draw gradient-ish rectangles
    for i in range(0, size[0], 20):
        draw.rectangle([i,0,i+10,size[1]], fill=(i % 256, (i*2) % 256, (i*3) % 256))
    img.save(path, 'JPEG')
    return path

def pil_to_np(path: str):
    img = Image.open(path).convert('RGB')
    return np.array(img)
