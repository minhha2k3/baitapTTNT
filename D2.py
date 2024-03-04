import numpy as np

# Tạo ma trận 3x3 M
M = np.array([[4, 5, 6],
              [7, 8, 9],
              [1, 2, 3]])

# Tạo vector v
v = np.array([1, 2, 3])

# Kiểm tra hạng (rank) và hình dạng (shape) của ma trận M và vector v
rank_M = np.linalg.matrix_rank(M)
shape_M = M.shape
shape_v = v.shape

print("Matrix M:")
print(M)
print("Rank of matrix M:", rank_M)
print("Shape of matrix M:", shape_M)

print("\nVector v:", v)
print("Shape of vector v:", shape_v)
