import numpy as np

# Vector x
x = np.array([2, 7])

# Tính độ dài của vector x (norm)
norm_x = np.linalg.norm(x)

# Chuẩn hóa vector x
normalized_x = x / norm_x

print("Vector x:", x)
print("Norm of vector x:", norm_x)
print("Normalized vector x:", normalized_x)
