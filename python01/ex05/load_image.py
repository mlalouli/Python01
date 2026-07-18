from __future__ import annotations
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ex_common.image_utils import ensure_sample, pil_to_np

def ft_load(path: str):
    # If requested path doesn't exist, create and use a sample image from ex_common
    if not os.path.exists(path):
        sample = ensure_sample('landscape.jpg', (257, 450))
        return pil_to_np(sample)
    return pil_to_np(path)

if __name__ == '__main__':
    p = ensure_sample('landscape.jpg', (257, 450))
    arr = ft_load(p)
    print(arr.shape)
