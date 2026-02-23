main_code = input("Enter your Code: ")
if len(main_code) <3:
    secret_code = main_code[::-1]
else:
    random_1= "bdd"
    random_2 ="dss"
    secret_code = random_1+ main_code[1:]+main_code[:1]+ random_2
print(secret_code)