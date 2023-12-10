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
    X = "X"
    Y = "Y"
    I = "I"
    
    def __repr__(self):
        return self.value

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
grid2 = []

for y, line in enumerate(fileinput.input()):
    grid.append([])
    grid2.append([])

    for x, char in enumerate(line.strip()):
        grid[y].append(PipeType(char))
        grid2[y].append(PipeType.GROUND)

start = (8, 42)
next1 = (8, 43)
previous1 = start
next2 = (9, 42)
previous2 = start

while next1 != next2:
    grid2[previous1[1]][previous1[0]] = grid[previous1[1]][previous1[0]]
    grid2[previous2[1]][previous2[0]] = grid[previous2[1]][previous2[0]]

    next1, previous1 = next_step(previous1, next1)
    next2, previous2 = next_step(previous2, next2)

grid2[previous1[1]][previous1[0]] = grid[previous1[1]][previous1[0]]
grid2[previous2[1]][previous2[0]] = grid[previous2[1]][previous2[0]]
grid2[next1[1]][next1[0]] = grid[next1[1]][next1[0]]

acc = 0
for y in range(len(grid2)):    
    iterator = iter(range(len(grid2[y])))
    
    for x in iterator:        
        if grid2[y][x] == PipeType.VERTICAL:
            grid2[y][x] = PipeType.X

        if grid2[y][x] == PipeType.SOUTH_EAST or grid2[y][x] == PipeType.NORTH_EAST:
            first = grid2[y][x]
            grid2[y][x] = PipeType.Y
            
            while True:
                x = next(iterator)
                if grid2[y][x] == PipeType.HORIZONTAL:
                    grid2[y][x] = PipeType.Y
                else:
                    if (first == PipeType.SOUTH_EAST and grid2[y][x] == PipeType.SOUTH_WEST) \
                        or (first == PipeType.NORTH_EAST and grid2[y][x] == PipeType.NORTH_WEST):
                        grid2[y][x] = PipeType.Y
                    else:
                        grid2[y][x] = PipeType.X
                    break

acc = 0
for y in range(len(grid2)):
    insied = False
    
    for x in range(len(grid2[y])):
        if grid2[y][x] == PipeType.GROUND and insied:
            acc += 1
            grid2[y][x] = PipeType.I
            
        if grid2[y][x] == PipeType.X:
            insied = not insied

print(acc)