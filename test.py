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
# m = int(input("Enter the number of month you want to find: "))
# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# pos = (m-1)*3
# print('The month is ',months[pos:pos+3])


# palindrome checker
# str = input("Enter an word: ")
# if (str==str[::-1]):
#     print(str+' is a palindrome')
# else:
#     print(str+' is not a plindrome')



# area of a triangle
# import math
# a = float(input('Enter the first Edge: '))
# b = float(input('Enter the second Edge: '))
# c = float(input('Enter the third Edge: '))
# if (a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0):
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     print("The area of the triangle {}".format(area))
# else:
#     print("The given edges cant form a triangle...")


# sum of 100 integers
sum = 0
for i in range(1,101):
    sum = sum+i
    
print(sum)