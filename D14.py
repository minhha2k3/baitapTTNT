import numpy as np

# Given vectors a1 and a2
a1 = np.array([1, -2, -5])
a2 = np.array([2, 5, 6])

# Create matrix M by stacking columns a1 and a2 horizontally
M = np.column_stack((a1, a2))

print("Matrix M:")
print(M)
