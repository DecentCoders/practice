# numA=int(input("Enter the first number: "))
# numB  =int( input ('Enter the second number:'))
# sum = numA+ numB
# average =sum/2
# print('The sum is:',sum ,end="")
# print('The average is:',average)
# money = int(input("Enter the amount of money: "))
# m50 = money//50
# money = money%50
# m5 = money//5
# money = money%5
# m1 = money
# print("The number of 50 notes: ",m50)
# print("The number of 5 notes: ", m5)
# print("The number of 1 notes: ",m1)


#finding month
m = int(input("Enter the number of month you want to find: "))
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
pos = (m-1)*3
print('The month is ',months[pos:pos+3])
