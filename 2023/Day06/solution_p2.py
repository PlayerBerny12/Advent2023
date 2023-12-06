races = [(54708275, 239114212951253)]

acc = 1
for race in races:
    max_distances = []  
    
    for i in range(race[0]):
        distance = i * (race[0] - i)
        max_distances.append(distance)    
    
    acc *= sum(i > race[1] for i in max_distances)

print(acc)