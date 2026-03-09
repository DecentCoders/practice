print("----Welcome to Hridoy's Library----")
while True:
    options =["Purchase Book", "Sell Book","Available books","Exit"]
    choices = [0,1,2,3]
    for i in range(len(options)):
        print(f'{i}:{options[i]}')
    user_choice = input("Enter your choice(0-3): ")
    if user_choice not in choices:
        print("Invalid choice, try again!. \n")       
        