import books
import purchase
import sell
#Color codes 
RED = "\033[1;31m"      
GREEN = "\033[1;32m"     
BLUE = "\033[1;34m"      
YELLOW = "\033[1;33m"    
PURPLE = "\033[1;35m"    
RESET = "\033[0m"        
print(f"{GREEN}----Welcome to Hridoy's Library----{RESET}")
while True:
    options =["Available books","Purchase Book", "Sell Book","Exit"]
    print(f"{BLUE}----Menu----{RESET}")
    for i,option in enumerate(options):
        print(f'{YELLOW}{i+1}:{RESET} {PURPLE}{option}{RESET}')
        
    try:
        user_choice = int(input(f"{BLUE}Enter your choice(0-3): {RESET}"))
    except ValueError:
        print(f"\n {RED}Invalid choice, try again. {RESET}\n")
        continue
 
    if user_choice < 0 or user_choice> len(options) :
        print(f"\n {RED}Invalid choice, Please select from menu {RESET}\n")
        continue
    elif user_choice == 1:
        books.avail_books()
    elif user_choice == 2:
        purchase.purchase_books()
    elif user_choice ==3:
        sell.sell_books()
    else:
        print(f"{RED}Exiting...{RESET}")
        break
    