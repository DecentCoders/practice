text = input("Enter a word or sentence: ")
lowertext = text.lower()
vowel_count = 0
for i in lowertext:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel_count += 1
print("the number of vowels is: ", vowel_count)