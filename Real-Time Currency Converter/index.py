import requests

def convert_currency():
    # Use a free API (this one is a common mock/public tester)
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json() # Convert the web response to a Python dictionary
        rates = data["rates"]

        print("--- USD Currency Converter ---")
        target = input("Enter target currency (e.g., EUR, GBP, JPY): ").upper()
        
        if target in rates:
            amount = float(input(f"How much USD do you want to convert to {target}? "))
            converted = amount * rates[target]
            print(f"💰 {amount} USD is equal to {converted:.2f} {target}")
        else:
            print("Sorry, that currency code was not found.")

    except Exception as e:
        print(f"Could not connect to the API: {e}")

convert_currency()