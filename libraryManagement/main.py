import books
import purchase
import sell
print("----Welcome to Hridoy's Library----")
while True:
    options =["Purchase Book", "Sell Book","Available books","Exit"]
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
        purchase.purchase_books()
    elif user_choice == 2:
        sell.sell_books()
    elif user_choice ==3:
        books.avail_books()
    else:
        print("Exiting...")
        break
    