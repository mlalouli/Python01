from __future__ import annotations
from typing import Any
import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    """Load an image from `path`, print its shape and return as a numpy array (H,W,C).

    Handles at least JPG/JPEG. Raises ValueError with clear message on error.
    """
    try:
        with Image.open(path) as img:
            img = img.convert('RGB')
            arr = np.array(img)
            print(f"The shape of image is: {arr.shape}")
            print(arr)
            return arr
    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")

def main():
    # simple smoke loader
    import os
    sample = os.path.join(os.path.dirname(__file__), 'landscape.jpg')
    if not os.path.exists(sample):
        # create a small sample image
        from PIL import ImageDraw
        img = Image.new('RGB', (10, 6), color=(19,42,83))
        draw = ImageDraw.Draw(img)
        draw.rectangle([0,0,4,2], fill=(23,42,84))
        img.save(sample, 'JPEG')
    ft_load(sample)

if __name__ == "__main__":
    main()
