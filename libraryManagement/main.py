import books
import purchase
import sell
import colors
print(f"{colors.GREEN}----Welcome to Hridoy's Library----{colors.RESET}")
while True:
    options =["Available books","Purchase Book", "Sell Book","Exit"]
    print(f"{colors.BLUE}----Menu----{colors.RESET}")
    for i,option in enumerate(options):
        print(f'{colors.YELLOW}{i+1}:{colors.RESET} {colors.PURPLE}{option}{colors.RESET}')
        
    try:
        user_choice = int(input(f"{colors.BLUE}Enter your choice(0-3): {colors.RESET}"))
    except ValueError:
        print(f"\n {colors.RED}Invalid choice, try again. {colors.RESET}\n")
        continue
 
    if user_choice < 0 or user_choice> len(options) :
        print(f"\n {colors.RED}Invalid choice, Please select from menu {colors.RESET}\n")
        continue
    elif user_choice == 1:
        books.avail_books()
    elif user_choice == 2:
        purchase.purchase_books()
    elif user_choice ==3:
        sell.sell_books()
    else:
        print(f"{colors.RED}Exiting...{colors.RESET}")
        break
    