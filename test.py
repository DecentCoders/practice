hobbies = [input("Enter a Hobbie: ") for i in range(5)]
print(hobbies)
with open("hobbies.txt", 'w') as file:
    file.write('\n'.join(hobbies))