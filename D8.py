# 8.a
import numpy as np

# Ma trận A đã cho
A = np.array([[2, 4, 9],
              [3, 6, 7]])

# Kiểm tra hạng của ma trận A
rank_A = np.linalg.matrix_rank(A)

# Kiểm tra hình dạng của ma trận A
shape_A = A.shape

print("Rank của ma trận A:", rank_A)
print("Hình dạng của ma trận A:", shape_A)

# 8.b
import numpy as np

# Ma trận A đã cho
A = np.array([[2, 4, 9],
              [3, 6, 7]])

# Kiểm tra hạng của ma trận A
rank_A = np.linalg.matrix_rank(A)

# Kiểm tra hình dạng của ma trận A
shape_A = A.shape

print("Rank của ma trận A:", rank_A)
print("Hình dạng của ma trận A:", shape_A)

# 8.c
# Trả về cột thứ hai của ma trận A
second_column_A = A[:, 1]

print("Cột thứ hai của ma trận A:", second_column_A)
