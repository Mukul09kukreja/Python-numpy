import numpy as np

array = np.array('A') # Zero Dimension
array = np.array(['A', 'B', 'C']) # 1 Dimension
array = np.array([['A', 'B', 'C'], ['D', 'F', 'E'], ['G', 'H', 'I']]) # 2D Dimensions
array = np.array([[['A', 'B', 'C'], ['D', 'F', 'E'], ['G', 'H', 'I']], [['A', 'B', 'C'], ['D', 'F', 'E'], ['G', 'H', 'I']]]) # 3 Dimension

# Shape like (3,3,3) means 3rows 3column 3rows inside column like 'A' in it 

print(array.ndim) # Check dimension of arrays
print(array.shape) # Check the shape of the arrays
print(array[0][0][0]) # Called as chain indexing 
print(array[0,0,0]) # Multi dimension indexing
 
# Note in Array we have equal no of elements in not 2 in one list 3 o other