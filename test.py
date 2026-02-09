name = input("Enter a name  to check: ")
found = False
with open('guests.txt','r') as file:
    for line in file:
        if line.strip() == name:
            found = True
            break
if found:
    print("Access Granted")
else:
    print("Access Denied")