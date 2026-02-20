main_code =input("Enter your Code: ")
if len(main_code)<3:
    secret_code = reversed(main_code)
else:
    secret_code = main_code
print(secret_code)