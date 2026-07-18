from __future__ import annotations
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import numpy as np
from PIL import Image
from ex_common.image_utils import ensure_sample, pil_to_np

def ft_load(path: str) -> np.ndarray:
    try:
        arr = pil_to_np(path)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        return arr
    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")

if __name__ == "__main__":
    # create sample
    p = ensure_sample('animal.jpeg', (768, 1024))
    ft_load(p)
