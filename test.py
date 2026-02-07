import time
def kbcGame():
    questions =[
    ["What is the name of the capital of Bangladesh?","Chittagong","Dhaka","Khulna","Rajshahi",2],
    ["What is the national flower of Bangladesh?","Rose","Sapla","Orange","Gandha",2],
    ["How many colors are there in the national flag of Bangladesh?","One","Two","Three","Four",2],
    ["When is Bangladesh's Independence Day celebrated?","March 26","December 16","February 21","April 14",1],
    ["In what year did the Liberation War of Bangladesh begin?","1969","1970","1971","1972",3],
    ["Who was the first president of Bangladesh?","Sheikh Mujibur Rahman","Tajuddin Ahmed","Syed Nazrul Islam","Khandaker Mushtaq Ahmed",1],
    ["How many square kilometers is the total area of ​​Bangladesh?"," 1,47,570","1,50,000","1,40,000","1,60,000",1],
    ["How many members are there in the National Parliament of Bangladesh?","300","350","400","250",2],
    ["Which is the highest award of Bangladesh?","Ekushey Padak","Freedom Award","National Film Award","Bangla Academy Award",2],
    ["Which is the largest river of Bangladesh?","Padma","Meghna","Brahmaputra","Karnaphuli",3]
    ]

    levels = ['1000','2000','3000','4000','5000','6000','7000','8000','9000','10000']
    money_won = 0
    print("------Who will be millionaire------")
    time.sleep(1)

    for i in range(len(questions)):
        current_qst = questions[i]
        print(f'\n Question for USD {levels[i]} :-')
        print(f' Q: {current_qst[0]}')
        print(f' 1. {current_qst[1]} \t 2. {current_qst[2]} \n 3. {current_qst[3]} \t 4. {current_qst[4]}')
        try:
            choice= int(input("Enter your choice (or 0 to quite with current prize money): "))
        except ValueError:
            print("Invalid input, Please enter a number...")
            break
        if choice == 0:
            print(f'Quiting...You are taking home USD {money_won}')
        elif choice == current_qst[5]:
            money_won = levels[i]
            print(f"Right answer.. You have won USD {money_won}")
        else:
            print(f"Wrong answer! The correct answer was {current_qst[5]}")
            print("You have lost everything...Sorry")
            break
        if money_won == levels[-1]:
            print("Congratulations You have completed the game. Thank you")
kbcGame()