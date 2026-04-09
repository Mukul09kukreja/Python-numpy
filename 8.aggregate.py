import numpy as np

# Aggregate functions = summarize data and typically
#                       return a single value
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array)) # Sum value
print(np.mean(array)) # Average value
print(np.std(array)) # Standard deviation
print(np.var(array)) # Variance
print(np.min(array)) # Minimum value
print(np.max(array)) # Maximum value
print(np.argmin(array)) # Position of min value
print(np.argmax(array)) # Position of max value

print(np.sum(array, axis=0)) # Sum of all columns
print(np.sum(array, axis=1)) # Sum of all rows