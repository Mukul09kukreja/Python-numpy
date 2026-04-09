import numpy as np

rng = np.random.default_rng(seed= 1) # Seed means how much time randomized

print(rng.integers(low=1, high=7)) # random number generator from 1 to 6
print(rng.integers(low=1, high=101, size= 3)) # Size menas how much number needed
print(rng.integers(low=1, high=101, size= (3, 2))) # Size with dimension