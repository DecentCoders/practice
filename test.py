names =['Hridoy','Hawladar','Rifat','Sajib','Riad']
with open ('guests.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')   
print("File 'guests.txt' has been created.")