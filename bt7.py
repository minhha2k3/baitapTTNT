for a in range(-2, 3):
    try:
        result = 10 / a
        print(f"10/{a} =", result)
    except ZeroDivisionError:
        print("Can't divide by zero")
