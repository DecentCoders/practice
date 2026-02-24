import random
import string
def encode(main_code):
    if len(main_code)<3:
        secret_code = main_code[::-1]
    else:
        random1 = "".join(random.choices(string.ascii_letters+string.digits,k=3))
        random2= "".join(random.choices(string.ascii_letters+string.digits,k=3))
        secret_code = random1 + main_code[1::]+main_code[:1]+ random2
    return secret_code
def decode(code):
    if len(code)<6:
        decoded = code[::-1]
    else:
        middle = code[3:-3]
        decoded = middle[-1]+middle[:-1]
    return decoded
encoded_code = False
while True:
    if encoded_code == False:
        main_code = input("Enter your code or 'Quite' to exite :").strip()
        if main_code.lower()=='quite':
            print("Exiting program..")
            break
    print("\n====Menu====")
    print("1: See your encoded code")
    print("2: Decode your code")
    print("3: Encode another code")
    print("4: Quite")
    
    options = input("Enter your choice (1/2/3): ").strip()
    
    if options == '1':
        encoded = encode(main_code)
        print(f"Encoded: {encoded}")
        encoded_code = True
    elif options =='2':
        encoded = encode(main_code)
        decoded_code = decode(encoded)
        print(f'Decoded code: {decoded_code}')
        encoded_code = True

    elif options =='3':
        encoded_code = False
    elif options == '4':
        print("Quiting..")
        break
    else:
        print("Invalid choice! Please enter 1,2,3")
    