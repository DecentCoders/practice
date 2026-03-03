import random
def snake_water_game():
    options = { "w":"water","s":"snake", "g":"gun"}
    print("-------------Snake Water Gun-------------------")
    print(options)
    choice =input("Enter your choice: ")
    if choice not in options:
        print("Invalid choice..Please choose s, w, or g.")
        return
    computer_choice = random.choice(["w","s","g"])
    print(f"you choosen {choice}")
    print(f'Computer chosed {computer_choice}')
    if choice == computer_choice:
        print("it's a draw..")
    elif (choice == "s" and computer_choice =="w") or (choice == "g" and computer_choice =="s") or ( choice == "w"  and computer_choice == "g"):
        print("Congratulation, You won..")
    else:
        print("Computer won, better luck next time")
    
if __name__ == "__main__":
    snake_water_game()