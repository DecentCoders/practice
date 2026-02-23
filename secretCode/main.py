import random
import string

def generate_random_string(length=3):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encode(main_code):
    if len(main_code) < 3:
        return main_code[::-1]
    else:
        random_1 = generate_random_string(3)
        random_2 = generate_random_string(3)
        return random_1 + main_code[1:] + main_code[:1] + random_2

def decode(secret_code):
    if len(secret_code) < 3:
        return secret_code[::-1]
    else:
        # Remove first 3 and last 3 characters (random padding)
        if len(secret_code) >= 6:
            middle = secret_code[3:-3]
            # Reconstruct: last char of middle + rest
            main_code = middle[-1] + middle[:-1]
            return main_code
        return "Invalid secret code"

while True:
    print("\n1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        main_code = input("Enter your Code: ")
        secret_code = encode(main_code)
        print(f"Secret Code: {secret_code}")
    elif choice == "2":
        secret_code = input("Enter the Secret Code: ")
        main_code = decode(secret_code)
        print(f"Original Code: {main_code}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")