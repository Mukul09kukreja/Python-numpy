import numpy as np

# Scaler arithmetic is used of single value for entire array

array = np.array([1,2,3])

print(array + 1) # Output: [2,3,4]

print(array - 1) # Output: [0,1,2]

print(array * 3) # Output: [3,6,9]

print(array / 4) # Output: [0.25,0.5,0.75]

print(array ** 5) # Output: [1, 32, 243]

# Vectorized math functions
array1 = np.array([1,2,3])
print(np.sqrt(array))

array2 = np.array([1.01, 2.5, 3.99])
print(np.round(array2))
# For round down use .floor
# For round up use .ceil
print(np.floor(array2))
print(np.ceil(array2))
# Some constants like pi
print(np.pi)


# Element wise arithmetic
array3 = np.array([1,2,3])
array4 = np.array([4,5,6])

print(array3 + array4) # Output: [5,7,9]
print(array3 - array4) # Output: [-3,-3,-3]
print(array3 * array4) # Output: [4,10,18]
print(array3 / array4) # Output: [0.25,0.4,0.5]
print(array3 ** array4) # Output: [1,32,729]


# Camparison Operator
scores = np.array([91,55,100,73,82,64])

print(scores == 100)
print(scores >= 100)
print(scores < 60)

# Ex: 
scores[scores < 60] = 0
print(scores)