import random
def snake_water_game():
    options = { "w":"water","s":"snake", "g":"gun"}
    print("-------------Snake Water Gun-------------------")
    print(options)
    outcomes = {
        ("s","w"): "you win!",
        ("g","s"): "you win!",
        ("w","g"): "you win!",
        ("w","s"): "Computer win!",
        ("s","g"): "Computer win!",
        ("g","w"): "Computer Win!"
    }
    user_score =0
    cmp_score =0
    while True:
        user_choice =input("Enter your choice (or q to quite): ")
        if user_choice == "q":
            print("Quiting..")
            break
        computer_choice = random.choice(["s","g","w"])
        print(f'your choice {user_choice} | computer choice {computer_choice}')
        
    
if __name__ == "__main__":
    snake_water_game()