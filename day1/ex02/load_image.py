from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("landscape.jpg")

# im.show()
pxarr = np.array(im)
print(f"The shape of the image is {pxarr.shape}")
print(im.format)
# print(pxarr)

# tarray = np.array([x for x in pxarr[0,:,:]], [x for x in pxarr[:,0,:]])
height, width, channels = pxarr.shape
tarray = np.zeros((width, height, channels), dtype=pxarr.dtype)


for i in range(width):
    tarray[i] = pxarr[:, i]


# newarr = pxarr[184:584, 312:712]
# print(f"The new shape of the image is {newarr.shape}")
# newim = Image.fromarray(newarr)
# newim.show()

invert = 255 - pxarr
plt.imshow(invert)
plt.show()
