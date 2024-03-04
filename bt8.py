ages = [23, 10, 80]
names = ["Hoa", "Lam", "Nam"]

sorted_tuples = sorted(zip(ages, names), key=lambda x: x[0])
print(sorted_tuples)
