import random
import string
main_code = input("Enter your code:")
def encode(main_code):
    if len(main_code)<3:
        secret_code = main_code[::-1]
    else:
        random1 = "".join(random.choices(string.ascii_letters+string.digits,k=3))
        random2= "".join(random.choices(string.ascii_letters+string.digits,k=3))
        secret_code = random1 + main_code[1::]+main_code[:1]+ random2
    return secret_code
def decode(code):
    if len(code)<3:
        decoded = code[::-1]
    else:
        middle = code[3:-3]
        decoded = middle[-1]+middle[:-1]
    return decoded
    
while True:
    encode(main_code)
    print("1:See your encoded code\n 2: Decode your code\n 3:Quite")
    options = input("Enter your choice: ")
    if options == 1:
        encoded_code = encode(main_code)
        print(encoded_code)
    elif options ==2:
        encoded_code = encode(main_code)
        decoded_code = decode(encoded_code)
    break
    