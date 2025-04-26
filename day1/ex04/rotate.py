import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
import sys


def ft_zoom(pxarr: np.array, w_size: int):
    # TODO : protect potential errors + make a correct export
    height = pxarr.shape[0]
    width = pxarr.shape[1]

    mid_y = height // 2
    mid_x = width // 2

    newarr = np.dot(
        pxarr[
            int(mid_y - w_size / 2) : int(mid_y + w_size / 2),
            int(mid_x - w_size / 2) : int(mid_x + w_size / 2),
            :3,
        ],
        [0.299, 0.587, 0.114],
    )

    print(f"The new shape of the image is {newarr.shape}")
    return newarr


def ft_rotate(pxarr: np.array):
    height, width, channels = pxarr.shape
    tarray = np.zeros((width, height, channels), dtype=pxarr.dtype)

    for i in range(width):
        tarray[i] = pxarr[:, i]

    return tarray


def main():
    img = ft_load("animal.jpeg")
    if img is None:
        sys.exit(1)
    print(img)
    plt.imshow(ft_zoom(ft_rotate(img), 400), cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
