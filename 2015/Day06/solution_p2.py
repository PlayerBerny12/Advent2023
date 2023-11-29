import sys
import re
from enum import Enum

class Command(str, Enum):
    TURNON = "turn on"
    TOGGLE = "toggle"
    TURNOFF = "turn off"

grid = [[0 for _ in range(1000)] for _ in range(1000)]
instructions = re.findall(r"(turn on|toggle|turn off)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)", sys.stdin.read())

for commnad, x1, y1, x2, y2 in instructions:
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2) + 1
    y2 = int(y2) + 1
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            if commnad == Command.TURNON:
                grid[x][y] += 1
            elif commnad == Command.TOGGLE:
                grid[x][y] += 2 
            elif commnad == Command.TURNOFF:
                if grid[x][y] > 0:
                    grid[x][y] -= 1
count = 0
for line in grid:
    count += sum(line)
    
print(count)