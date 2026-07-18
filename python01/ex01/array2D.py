from __future__ import annotations
from typing import List

def slice_me(family: List[List[float]], start: int, end: int) -> List[List[float]]:

    if not isinstance(family, list) or any(not isinstance(row, list) for row in family):
        raise ValueError("family must be a 2D list")
    if len(family) == 0:
        print("My shape is : (0, 0)")
        print("My new shape is : (0, 0)")
        return []
    n_rows = len(family)
    n_cols = len(family[0])
    if any(len(row) != n_cols for row in family):
        raise ValueError("family must be rectangular (all rows same length)")
    print(f"My shape is : ({n_rows}, {n_cols})")
    sliced = family[start:end]
    print(f"My new shape is : ({len(sliced)}, {n_cols})")
    return sliced

def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()
