import fileinput
import re

file = fileinput.input()
seeds = re.findall(r"\d+", file.readline())
maps = [[],[],[],[],[],[],[]]

category = 0

file.readline()
file.readline()
for line in file:
    if line == "\n":
        category += 1
        file.readline()
        continue

    map = re.findall(r"\d+", line)

    destination = int(map[0])
    source = int(map[1])
    count = int(map[2])    

    maps[category].append((source, destination, count))
    
locations = []
for seed in seeds:
    seed = int(seed)
    found = False
    
    for map_range in maps[0]:
        if seed >= map_range[0] and seed <= map_range[0] + map_range[2]:
            result = seed + (map_range[1] - map_range[0])
            found = True
            break
    
    if not found:
        result = seed

    for i in range(1, 7):
        found = False
    
        for map_range in maps[i]:            
            if result >= map_range[0] and result <= map_range[0] + map_range[2]:
                result = result + (map_range[1] - map_range[0])
                found = True
                break
        
        if not found:
            result = result
    locations.append(result)
    
print(min(locations))
