import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def ft_invert(pxarr: np.array) -> np.array:
    return 255 - pxarr

def ft_red(pxarr: np.array) -> np.array:
    return pxarr * [1, 0, 0]

def ft_green(pxarr: np.array) -> np.array:
    return pxarr - ft_red(pxarr) - ft_blue(pxarr)

def ft_blue(pxarr: np.array) -> np.array:
    blue = pxarr.copy()
    blue[:,:,:2] = 0
    return blue

def ft_grey(pxarr: np.array) -> np.array:
    return pxarr[:,:,0]

def ft_pimp(pxarr: np.array):

    plt.subplot(3, 2, 1)
    plt.imshow(ft_invert(pxarr), cmap="gray")
    plt.title("invert image")
    plt.subplot(3, 2, 2)
    # plt.imshow(ft_green(pxarr), cmap="gray")
    plt.title("green image")
    plt.subplot(3, 2, 3)
    plt.imshow(ft_blue(pxarr), cmap="gray")
    plt.subplot(3, 2, 4)
    plt.imshow(pxarr, cmap="gray")


def main():
    img = ft_load("landscape.jpg")
    ft_pimp(img)
    plt.show()


if __name__ == "__main__":
    main()
