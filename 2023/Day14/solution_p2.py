import fileinput
import numpy as np
from collections import Counter

def move(grid, left):
    for y in range(len(grid)):
        if left:
            move_position = 0
            sequence = range(len(grid[y]))
        else:
            move_position = len(grid[y]) - 1
            sequence = range(move_position, -1, -1)

        for x in sequence:
            if grid[y][x] == "#":
                move_position = x + 1 if left else x - 1
            elif grid[y][x] == "O":                
                grid[y][x] = "."                
                grid[y][move_position] = "O"
                move_position =  move_position + 1 if left else move_position - 1
                
    return grid

cache = {}
step = 0
cycles = 1_000_000_000
grid = np.array([[char for char in line.strip()] for line in fileinput.input()])

while step < cycles:
    step += 1

    grid = move(grid.T, True).T        
    grid = move(grid, True)
    grid = move(grid.T, False).T
    grid = move(grid, False)

    key = "".join([char for char in grid.flatten()])

    if key in cache:
        period = step - cache[key]        
        step += ((cycles - step) // period) * period

    cache[key] = step

acc = 0
for i in range(len(grid)):
    counter = Counter(grid[i])
    acc += (len(grid) - i) * counter["O"]

print(acc)