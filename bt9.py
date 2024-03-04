# 9.a and b
file_path = "firstname.txt"

try:
    with open(file_path, 'r') as file:
        print("Contents of 'firstname.txt':")
        for line in file:
            print(line.strip())  # strip() để loại bỏ khoảng trắng và ký tự xuống dòng thừa
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error occurred while trying to read file '{file_path}'.")


# 9.c
file_path = "firstname.txt"

try:
    with open(file_path, 'r') as file:
        print("Contents of 'firstname.txt':")
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error occurred while trying to read file '{file_path}'.")
