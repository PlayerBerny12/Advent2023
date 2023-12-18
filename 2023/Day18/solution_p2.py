import fileinput
from enum import Enum

class Direction(int, Enum):
    UP = 3
    DOWN = 1
    LEFT = 2
    RIGHT = 0

plan = []
vertices = []
perimeter = 0
x, y = (0, 0)

for line in fileinput.input():
    _, _, color = line.strip().split(" ")
    color = color[2:-1]
    direction = int(color[-1])
    length = int(color[0:-1], 16) 
    
    if direction == Direction.UP:
        y -= length
    elif direction == Direction.DOWN:
        y += length
    elif direction == Direction.LEFT:
        x -= length
    elif direction == Direction.RIGHT:
        x += length
    
    perimeter += length 
    vertices.append((x, y))
    
acc = 0
for i in range(len(vertices)):
    x1, y1 = vertices[i]
    if i + 1 < len(vertices):
        x2, y2 = vertices[i+1]
    else:
        x2, y2 = vertices[0]
    
    acc += x1 * y2 - x2 * y1
    
print(acc // 2 + perimeter // 2 + 1)