import fileinput
from enum import Enum

class Direction(str, Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

line = fileinput.input().readline()

grid = [[0 for _ in range(len(line))] for _ in range(len(line))]
x = 0
y = 0
grid[x][y] = 1

for char in line:
    if char == Direction.UP:
        x += 1
    elif char == Direction.DOWN:
        x -= 1
    elif char == Direction.LEFT:
        y -= 1
    elif char == Direction.RIGHT:
        y += 1

    grid[x][y] += 1

count = 0
for line in grid:
    for cell in line:
        if cell > 0:
            count += 1

print(count)