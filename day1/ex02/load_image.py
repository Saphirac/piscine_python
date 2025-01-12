from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("animal.jpeg")

# im.show()
pxarr = np.asarray(im)
print(f'The shape of the image is {pxarr.shape}')
print(im.format)
print(pxarr)

newarr = pxarr[184:584,312:712]
print(f'The new shape of the image is {newarr.shape}')
newim = Image.fromarray(newarr)
# newim.show()

plt.imshow(newarr)
plt.show()
