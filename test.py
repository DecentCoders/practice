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