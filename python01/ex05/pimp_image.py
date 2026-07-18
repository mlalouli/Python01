from __future__ import annotations
import numpy as np

def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the colors of the image received."""
    if not isinstance(array, np.ndarray):
        raise ValueError('array must be numpy.ndarray')
    # invert per-channel
    return 255 - array

def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only red channel, zero others."""
    a = array.copy()
    if a.ndim == 3:
        a[:, :, 1] = 0
        a[:, :, 2] = 0
    return a

def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only green channel, zero others."""
    a = array.copy()
    if a.ndim == 3:
        a[:, :, 0] = 0
        a[:, :, 2] = 0
    return a

def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only blue channel, zero others."""
    a = array.copy()
    if a.ndim == 3:
        a[:, :, 0] = 0
        a[:, :, 1] = 0
    return a

def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert image to greyscale (average method)."""
    if not isinstance(array, np.ndarray):
        raise ValueError('array must be numpy.ndarray')
    if array.ndim == 3:
        grey = array.mean(axis=2).astype(np.uint8)
        return grey
    return array
