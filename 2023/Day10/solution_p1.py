import fileinput
from enum import Enum

class PipeType(str, Enum):
    VERTICAL = "|"
    HORIZONTAL = "-"
    NORTH_EAST = "L"
    NORTH_WEST = "J"
    SOUTH_WEST = "7"
    SOUTH_EAST = "F"
    GROUND = "."    
    START = "S"

def next_step(previous_coordination, actual_coordination):
    x1, y1 = previous_coordination
    x2, y2 = actual_coordination
    
    pipe_type = grid[y2][x2]

    if pipe_type == PipeType.VERTICAL:
        if y1 == y2 - 1:
            return (x2, y2 + 1), actual_coordination
        else:
            return (x2, y2 - 1), actual_coordination
    elif pipe_type == PipeType.HORIZONTAL:
        if x1 == x2 - 1:
            return (x2 + 1, y2), actual_coordination
        else:
            return (x2 - 1, y2), actual_coordination
    elif pipe_type == PipeType.NORTH_EAST:
        if x1 == x2 and y1 == y2 - 1:
            return (x2 + 1, y2), actual_coordination
        else:
            return (x2, y2 - 1), actual_coordination
    elif pipe_type == PipeType.NORTH_WEST:
        if x1 == x2 and y1 == y2 - 1:
            return (x2 - 1, y2), actual_coordination
        else:
            return (x2, y2 - 1), actual_coordination
    elif pipe_type == PipeType.SOUTH_WEST:
        if x1 == x2 and y1 == y2 + 1:
            return (x2 - 1, y2), actual_coordination
        else:
            return (x2, y2 + 1), actual_coordination
    elif pipe_type == PipeType.SOUTH_EAST:
        if x1 == x2 and y1 == y2 + 1:
            return (x2 + 1, y2), actual_coordination
        else:
            return (x2, y2 + 1), actual_coordination

grid = []
start = None
for y, line in enumerate(fileinput.input()):
    grid.append([])
    
    for x, char in enumerate(line.strip()):
        pipe_type = PipeType(char)
        if pipe_type == PipeType.START:
            start = x, y
        
        grid[y].append(pipe_type)

next1 = (8, 43)
previous1 = start
next2 = (9, 42)
previous2 = start

step = 1
while next1 != next2:
    next1, previous1 = next_step(previous1, next1)
    next2, previous2 = next_step(previous2, next2)
    step += 1

print(step)