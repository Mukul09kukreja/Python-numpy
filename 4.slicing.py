import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])


# array[start:end:step] = slice operator

# Row selection
print(array[0:4:2])
print(array[::-1])

# Column Selection
print(array[:, 0])

print(array[:, 0:3])

print(array[:, 1::2])

print(array[0:2, 0:2]) # it is like array[rows, column]