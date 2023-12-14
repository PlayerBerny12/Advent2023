import fileinput
import numpy as np

def find_mirrors(patterns, tollerance):    
    acc = 0
    for i in range(len(patterns) - 1):
        j1 = i
        j2 = i+1
        
        while len(patterns[j1]) - sum(patterns[j1] == patterns[j2]) <= tollerance:
            j1 -= 1
            j2 += 1
            
            if j1 == -1 or j2 == len(patterns):
                acc += i + 1
                break
    return acc

patterns = []
acc = 0 
acc2 = 0
for line in fileinput.input():
    line = line.strip()
    if line == "":
        patterns = np.array(patterns)        
                
        row_mirrors = find_mirrors(patterns, 0)
        column_mirrors = find_mirrors(patterns.T, 0)
        
        acc += row_mirrors * 100
        acc += column_mirrors

        row_mirrors = find_mirrors(patterns, 1)
        column_mirrors = find_mirrors(patterns.T, 1)
        
        acc2 += row_mirrors * 100
        acc2 += column_mirrors

        patterns = []
    else:
        patterns.append([])
        for char in line:
            patterns[-1].append(char)        

print(acc2 - acc)