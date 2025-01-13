from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    im = Image.open(path)
    pxarr = np.array(im)
    print(f"The shape of the image is {pxarr.shape}")
    print(im.format)
    return pxarr
