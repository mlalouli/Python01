from __future__ import annotations
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ex_common.image_utils import ensure_sample, pil_to_np

def transpose_manual(arr):
    """Transpose a 2D array or a 3D (H,W,1) array manually without using numpy.transpose."""
    if arr.ndim == 3 and arr.shape[2] == 1:
        h, w, _ = arr.shape
        out = [[0]*h for _ in range(w)]
        for i in range(h):
            for j in range(w):
                out[j][i] = int(arr[i, j, 0])
        return out
    elif arr.ndim == 2:
        h, w = arr.shape
        out = [[0]*h for _ in range(w)]
        for i in range(h):
            for j in range(w):
                out[j][i] = int(arr[i, j])
        return out
    else:
        raise ValueError('Unsupported array shape for transpose_manual')

def main():
    path = ensure_sample('animal.jpeg', (400, 400))
    arr = pil_to_np(path)
    # crop center 400x400 and keep single channel
    h, w = arr.shape[:2]
    size = min(400, h, w)
    y0 = (h - size)//2
    x0 = (w - size)//2
    cropped = arr[y0:y0+size, x0:x0+size]
    if cropped.ndim == 3:
        cropped = cropped[:, :, 0:1]
    print(f"The shape of image is: {cropped.shape}")
    print(cropped)
    transposed = transpose_manual(cropped)
    print(f"New shape after Transpose: ({len(transposed)}, {len(transposed[0])})")
    # print partial view
    print(transposed[:3])

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
