import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def main():
    path = os.path.join(os.path.dirname(__file__), 'landscape.jpg')
    arr = ft_load(path)
    inv = ft_invert(arr)
    r = ft_red(arr)
    g = ft_green(arr)
    b = ft_blue(arr)
    grey = ft_grey(arr)
    print(ft_invert.__doc__)
    # Print shapes to verify
    print(arr.shape, inv.shape if hasattr(inv, 'shape') else None)

if __name__ == '__main__':
    main()
