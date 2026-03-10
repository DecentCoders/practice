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
print("----Welcome to Hridoy's Library----")
while True:
    options =["Available books","Purchase Book", "Sell Book","Exit"]
    print("----Menu----")
    for i,option in enumerate(options):
        print(f'{i+1}: {option}')
        
    try:
        user_choice = int(input("Enter your choice(0-3): "))
    except ValueError:
        print("\n Invalid choice, try again. \n")
        continue
 
    if user_choice < 0 or user_choice> len(options) :
        print("\n Invalid choice, Please select from menu\n")
        continue
    elif user_choice == 1:
        books.avail_books()
    elif user_choice == 2:
        purchase.purchase_books()
    elif user_choice ==3:
        sell.sell_books()
    else:
        print("Exiting...")
        break
    