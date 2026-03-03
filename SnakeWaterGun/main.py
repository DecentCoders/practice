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
    
    
snake_water_game()