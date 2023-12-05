import fileinput
import re
import os
import sys
from multiprocessing import Pool

def task(i):
    locations = sys.maxsize
    start = int(seeds[i])
    length = int(seeds[i + 1])

    for j in range(start, start + length):
        seed = j        
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
        if result < locations:
            locations = result        
    
    print(locations)
    return locations

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
    
pool = Pool(os.cpu_count()-1)     
print(min(pool.map(task, range(0, len(seeds), 2))))
