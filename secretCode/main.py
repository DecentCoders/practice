main_code = input("Enter your Code: ")
if len(main_code) <3:
    secret_code = main_code[::-1]
else:
    secret_code = "".random().join(main_code).random()
print(secret_code)