import numpy as np

rng = np.random.default_rng()

array = np.array([1,2,3,4,5])

rng.shuffle(array)

# .shuffle method use to shuffle this array elements
print(array)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])

fruits = rng.choice(fruits)

# .choice use to select any random number of an array

print(fruits)