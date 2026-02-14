import csv

def calculate_profit(price, qty):
    """Simple function to handle the math."""
    return float(price) * int(qty)

def process_sales(filename):
    category_totals = {}

    try:
        with open(filename, "r") as f:
            # DictReader treats each row as a dictionary
            reader = csv.DictReader(f)
            
            for row in reader:
                # 1. Logic: Skip anything that was 'Returned'
                if row["Status"] == "Returned":
                    continue
                
                # 2. Manipulation: Use our function to get the row total
                profit = calculate_profit(row["Price"], row["Quantity"])
                
                # 3. Grouping: Add to the specific category in our dictionary
                cat = row["Category"]
                category_totals[cat] = category_totals.get(cat, 0) + profit

        # 4. Output: Show the final results
        print("--- Sales Summary by Category ---")
        for category, total in category_totals.items():
            print(f"{category}: ${total:,.2f}")

    except FileNotFoundError:
        print("File not found! Make sure sales.csv exists.")

# To run this, ensure the csv file is created first
process_sales("sales.csv")