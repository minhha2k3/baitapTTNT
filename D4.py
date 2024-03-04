import numpy as np

# Ma trận M ban đầu
M = np.array([[4, 5, 6],
              [7, 8, 9],
              [1, 2, 3]])

# Vector v ban đầu
v = np.array([1, 2, 3])

# Chuyển vị của ma trận M
M_transpose = M.T  # hoặc np.transpose(M)

# Chuyển vị của vector v
v_transpose = v.T  # hoặc np.transpose(v)

print("Transpose of matrix M:")
print(M_transpose)
print("Shape of transpose of matrix M:", M_transpose.shape)

print("\nTranspose of vector v:")
print(v_transpose)
print("Shape of transpose of vector v:", v_transpose.shape)
