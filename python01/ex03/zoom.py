from __future__ import annotations
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ex_common.image_utils import ensure_sample, pil_to_np
import numpy as np

def main():
    path = ensure_sample('animal.jpeg', (768, 1024))
    arr = pil_to_np(path)
    print(f"The shape of image is: {arr.shape}")
    print(arr)
    # take a square ~400x400 from center
    h, w = arr.shape[:2]
    size = 400
    y0 = (h - size)//2
    x0 = (w - size)//2
    cropped = arr[y0:y0+size, x0:x0+size]
    # if RGB, convert to single channel
    if cropped.ndim == 3:
        cropped = cropped[:, :, 0:1]
    print(f"New shape after slicing: {cropped.shape}")
    print(cropped)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
