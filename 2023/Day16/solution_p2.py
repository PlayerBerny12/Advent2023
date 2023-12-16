import fileinput
from copy import deepcopy
from enum import Enum

class Direction(str, Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    def __repr__(self):
        return self.value
    
GRID_SIZE = 110
DIRECTION_MAP = {
    "\\" : { "^": [Direction.LEFT], "v": [Direction.RIGHT], "<": [Direction.UP], ">": [Direction.DOWN] },
    "/" : { "^": [Direction.RIGHT], "v": [Direction.LEFT], "<": [Direction.DOWN], ">": [Direction.UP] },
    "|" : { "^": [Direction.UP], "v": [Direction.DOWN], "<": [Direction.UP, Direction.DOWN], ">": [Direction.UP, Direction.DOWN] },
    "-" : { "^": [Direction.LEFT, Direction.RIGHT], "v": [Direction.LEFT, Direction.RIGHT], "<": [Direction.LEFT], ">": [Direction.RIGHT] },
}

def beam_step(grid, direction_in, x, y):
    grid_field = grid[y][x][0]
    beams_out = []
    
    if grid_field == ".":
        directions_out = [direction_in]
    else:
        directions_out = DIRECTION_MAP[grid_field][direction_in]

    for direction_out in directions_out:
        if direction_out == Direction.UP:
            beams_out.append((direction_out, x, y - 1))
        elif direction_out == Direction.DOWN:
            beams_out.append((direction_out, x, y + 1))
        elif direction_out == Direction.LEFT:
            beams_out.append((direction_out, x - 1, y))
        elif direction_out == Direction.RIGHT:
            beams_out.append((direction_out, x + 1, y))

    return beams_out
    
max = 0
grid = [[(char, []) for char in line.strip()] for line in fileinput.input()]

for direction in [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]:
    for i in range(GRID_SIZE):    
        grid_copy = deepcopy(grid)

        if direction == Direction.DOWN:
            beams = [(direction, i, 0)]
        elif direction == Direction.UP:
            beams = [(direction, i, GRID_SIZE - 1)]
        elif direction == Direction.RIGHT:
            beams = [(direction, 0, i)]
        elif direction == Direction.LEFT:
            beams = [(direction, GRID_SIZE-1, i)]

        while len(beams) > 0:
            direction_in, x_in, y_in = beams[0]
            beams_next = beam_step(grid_copy, direction_in, x_in, y_in)
            
            for beam_next in beams_next:
                direction_out, x_out, y_out = beam_next
                if beam_next[0] not in grid_copy[y_in][x_in][1]:
                    grid_copy[y_in][x_in][1].append(direction_out)
                    
                    if 0 <= x_out < GRID_SIZE and 0 <= y_out < GRID_SIZE:
                        beams.append(beam_next)

            del beams[0]

        acc = 0
        for line in grid_copy:
            for field in line:
                if len(field[1]) > 0:
                    acc += 1   

        if max < acc:
            max = acc

print(max)