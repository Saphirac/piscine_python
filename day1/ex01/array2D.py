import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    arr = np.array(family)
    print("My shape is :", arr.shape)
    newarr = arr[start:end]
    print("My new shape is :", newarr.shape)
    return family[start:end]

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
