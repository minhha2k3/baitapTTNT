import numpy as np

# Given matrix A
A = np.array([[1, 1, 2],
              [2, 4, -3],
              [3, 6, -5]])

# Compute the determinant of matrix A
determinant_A = np.linalg.det(A)

print("Determinant of matrix A:", determinant_A)
