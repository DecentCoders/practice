try:
    minutes = int(input("Enter the minutes: "))
except:
    print("Invalid Input")
    minutes = 0  

def num_banana(minutes):
    total_banana = 0
    for minute in range(1, minutes + 1):
        total_banana += minute
        if total_banana % 7 == 0 and total_banana >= 3:
            total_banana -= 3  # Drop 3 bananas
    
    return total_banana
if minutes < 0:
    print("Minutes can't be negative")
elif minutes == 0:
    print(0)  
else:
    total_bananas = num_banana(minutes)
    print(total_bananas)