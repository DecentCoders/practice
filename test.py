temps = [15, 22, 18, 25, 30, 12, 27]
warm_temps =[]
for t in temps:
    if t > 20:
        warm_temps.append(t)
for temp in warm_temps:
    print(f'Safe temperature: {temp}')