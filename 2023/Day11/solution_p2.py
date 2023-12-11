import fileinput
import itertools
import numpy as np

EXPANSION_SPEED = 1000000 - 1

def expand(grid):
    empty_cols = []
    for i in range(len(grid[0])):
        if np.all(grid[:, i] == "."):
            empty_cols.append(i)

    empty_rows = []
    for i in range(len(grid)):
        if np.all(grid[i] == "."):
            empty_rows.append(i)    

    return empty_rows, empty_cols

def distanec(galaxy1, galaxy2, empty_rows, empty_cols):
    min_x = min(galaxy1[0], galaxy2[0])
    max_x = max(galaxy1[0], galaxy2[0])
    min_y = min(galaxy1[1], galaxy2[1])
    max_y = max(galaxy1[1], galaxy2[1])

    cross_y = len(list(filter(lambda a: min_x < a < max_x, empty_cols)))
    cross_x = len(list(filter(lambda a: min_y < a < max_y, empty_rows)))
      
    return (abs(galaxy1[0] - galaxy2[0]) + (cross_y * EXPANSION_SPEED)) + (abs(galaxy1[1] - galaxy2[1]) + (cross_x * EXPANSION_SPEED))


grid = np.array([[char for char in line.strip()] for line in fileinput.input()])
empty_rows, empty_cols = expand(grid)
galaxies = []

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            galaxies.append((x, y))

acc = 0
for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
    acc += distanec(galaxy1, galaxy2, empty_rows, empty_cols)

print(acc)