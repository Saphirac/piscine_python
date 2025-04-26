import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
import matplotlib.font_manager as fm
import sys

font_prop = fm.FontProperties(fname="times.ttf")
fig, axs = plt.subplots(nrows=3, ncols=2, subplot_kw={"xticks": [], "yticks": []})


def ft_invert(pxarr: np.array) -> np.array:
    """Inverts the color of the image received."""
    invert = 255 - pxarr
    axs[0, 1].imshow(invert, cmap="gray")
    axs[0, 1].set_title("Invert figure", fontsize=14, fontproperties=font_prop, y=-0.22)
    print(invert)
    return invert


def ft_red(pxarr: np.array) -> np.array:
    """Turns red the color of the image received."""
    red = pxarr * [1, 0, 0]
    axs[1, 0].imshow(red, cmap="gray")
    axs[1, 0].set_title("red figure", fontsize=12, fontname="Liberation Sans", y=-0.22)
    print(red)
    return red


def ft_green(pxarr: np.array) -> np.array:
    """Turns green the color of the image received."""
    green = pxarr - ft_red(pxarr) - ft_blue(pxarr)
    axs[1, 1].imshow(green, cmap="gray")
    print(green)
    return green


def ft_blue(pxarr: np.array) -> np.array:
    """Turns blue the color of the image received."""
    blue = pxarr.copy()
    blue[:, :, :2] = 0
    axs[2, 0].imshow(blue, cmap="gray")
    print(blue)
    return blue


def ft_grey(pxarr: np.array) -> np.array:
    """Turns grey the color of the image received."""
    grey = pxarr[:, :, 0]
    axs[2, 1].imshow(grey, cmap="gray")
    print(grey)
    return grey


def main():
    plt.rcParams["font.family"] = "Times New Roman"
    img = ft_load("day1/landscape.jpg")
    if img is None:
        sys.exit(1)
    axs[0, 0].imshow(img, cmap="gray")
    ft_invert(img)
    ft_red(img)
    ft_green(img)
    ft_blue(img)
    ft_grey(img)
    plt.show()


if __name__ == "__main__":
    main()
