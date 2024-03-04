import numpy as np

# Các vector đã cho
a = np.array([10, 15])
b = np.array([8, 2])
c = np.array([1, 2, 3])

# Tính toán phép cộng vector a + b
tong_ab = a + b

# Tính toán phép trừ vector a - b
hieu_ab = a - b

# Tính toán phép trừ vector a - c
try:
    hieu_ac = a - c
except ValueError as e:
    hieu_ac = None
    print("Lỗi:", e)

# In kết quả
print("a + b:", tong_ab)
print("a - b:", hieu_ab)
print("a - c:", hieu_ac)

# Lỗi này cho biết rằng phép toán không thể thực hiện được vì hình dạng của các mảng không tương thích cho việc broadcasting. Cụ thể, toán hạng thứ hai (c) có hình dạng khác biệt so với toán hạng thứ nhất (a), vì vậy phép toán không thể được thực hiện.
