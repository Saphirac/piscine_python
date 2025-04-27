from PIL import Image
import numpy as np
import sys


def ft_load(path: str) -> np.array:
    im = Image.open(path)
    pxarr = np.array(im)
    print(f"The shape of the image is {pxarr.shape}")
    print(im.format)
    return pxarr


def main():
    img = ft_load("day1/aeimal.jpeg")
    if img is None:
        sys.exit(1)
    print(img)


if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main()
    except FileNotFoundError as e:
        print(f"{e.__class__.__name__}: file doesn't exist")
