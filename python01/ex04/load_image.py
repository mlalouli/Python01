from __future__ import annotations
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ex_common.image_utils import ensure_sample, pil_to_np

def ft_load(path: str):
    return pil_to_np(path)

if __name__ == "__main__":
    p = ensure_sample('animal.jpeg', (400, 400))
    arr = ft_load(p)
    print(arr.shape)
