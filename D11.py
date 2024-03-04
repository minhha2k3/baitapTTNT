#a
import numpy as np

# Tạo ma trận ngẫu nhiên 3x3 với giá trị trong phạm vi (1, 10)
random_matrix = np.random.randint(1, 10, size=(3, 3))

# Tính trị chéo của ma trận bằng một lệnh
trace_a = np.trace(random_matrix)

print("Ma trận ngẫu nhiên 3x3:")
print(random_matrix)
print("Trị chéo của ma trận (cách a):", trace_a)

#b
# Tính trị chéo của ma trận bằng vòng lặp
trace_b = 0
for i in range(3):
    trace_b += random_matrix[i, i]

print("Trị chéo của ma trận (cách b):", trace_b)
