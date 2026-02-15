cities = ["London", "Paris", "New York", "Tokyo", "Sydney"]
with open("cities.txt","w") as file:
    for city in cities:
        file.write(city +"\n")