main_code = input("Enter your Code: ")
if len(main_code) <3:
    secret_code = ''.join(reversed(main_code))
print(secret_code)