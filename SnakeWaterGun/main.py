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
        user_choice =input("\n Enter your choice (or q to quite): ")
        if user_choice not in options:
            print("Invalid choice, Only input s,g,w")
            continue
        elif user_choice == "q":
            print("Quiting..")
            break
        
        computer_choice = random.choice(["s","g","w"])
        print(f'your choice - {user_choice} | computer choice - {computer_choice}')
        result = outcomes.get((user_choice,computer_choice),"It's a Draw..")
        print(result)
        points = {"you win!": (1,0),"Computer Win!":(0,2),"its a draw": (0,0)}
        u_pts, cpts = points.get(result,(0,0))
        user_score += u_pts
        cmp_score +=cpts
        print(f" Your score: {user_score} | Computer Score: {cmp_score}")
        if user_score >=5:
            print("Congratulation You won..")
            break
        elif cmp_score >=5:
            print("Computer Won, better luck next time!")
            break
    
if __name__ == "__main__":
    snake_water_game()