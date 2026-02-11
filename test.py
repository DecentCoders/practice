import json

def save_data(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def load_data():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def main():
    expenses = load_data()
    
    while True:
        print("\n1. Add Expense  2. View Summary  3. Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            item = input("What did you buy? ")
            price = float(input("How much did it cost? "))
            category = input("Category (Food/Fun/Bills): ")
            expenses.append({"item": item, "price": price, "category": category})
            save_data(expenses)
            
        elif choice == "2":
            # CHALLENGE: Write logic to print total spending here!
            total = sum(e['price'] for e in expenses)
            print(f"Total spent: ${total:.2f}")
            
        elif choice == "3":
            break

if __name__ == "__main__":
    main()