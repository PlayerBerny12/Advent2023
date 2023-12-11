import fileinput
import itertools
import numpy as np

def expand(grid):
    empty_cols = []
    for i in range(len(grid[0])):
        if np.all(grid[:, i] == "."):
            empty_cols.append(i)

    empty_rows = []
    for i in range(len(grid)):
        if np.all(grid[i] == "."):
            empty_rows.append(i)
    
    for idx, col in enumerate(empty_cols):
        grid = np.insert(grid, col + idx, ".", axis=1)

    for idx, col in enumerate(empty_rows):
        grid = np.insert(grid, col + idx, ".", axis=0)

    return grid

grid = np.array([[char for char in line.strip()] for line in fileinput.input()])
grid = expand(grid)
galaxies = []

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            galaxies.append((x, y))

acc = 0
for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
    acc += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
print(acc)