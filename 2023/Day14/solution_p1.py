import fileinput
import numpy as np
from collections import Counter

def move(grid):
    for y in range(len(grid)):
        move_position = 0

        for x in range(len(grid[y])):            
            if grid[y][x] == "#":
                move_position = x + 1
            elif grid[y][x] == "O":                
                grid[y][x] = "."                
                grid[y][move_position] = "O"
                move_position += 1                
                
    return grid

grid = np.array([[char for char in line.strip()] for line in fileinput.input()])
grid = move(grid.T).T

acc = 0
for i in range(len(grid)):
    counter = Counter(grid[i])    
    acc += (len(grid) - i) * counter["O"]

print(acc)