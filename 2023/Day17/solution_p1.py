import fileinput
import sys
from heapq import heappop, heappush

class Node():
    def __init__(self, previous, position, direction, straight_count, heat_loss):
        self.previous = previous
        self.position = position
        self.direction = direction
        self.straight_count = straight_count

        if previous != None:
            self.heat_loss_acc = previous.heat_loss_acc + heat_loss
        else:
            self.heat_loss_acc = 0
    
    def key(self):
        return (self.position, self.direction, self.straight_count)

    def __lt__(self, other):
        return self.heat_loss_acc < other.heat_loss_acc
    
    def __eq__(self, other):
        if other != None:
            return self.position == other.position
        else:
            return False    
    
    def __repr__(self) -> str:
        return f"{self.heat_loss_acc}"

def generate_steps(grid, node):
    steps = []
    
    for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        position = (node.position[0] + direction[0], node.position[1] + direction[1])        

        if not (0 <= position[0] < len(grid[0]) and 0 <= position[1] < len(grid)):
            continue

        if node.direction == direction:
            new_step = Node(node, position, direction, node.straight_count + 1, grid[position[1]][position[0]])
        else:
            new_step = Node(node, position, direction, 1, grid[position[1]][position[0]])

        if new_step == node.previous or new_step.straight_count > 3:
            continue

        steps.append(new_step)
    
    return steps

def search(grid, start):
    start_node = Node(None, start, None, 0, 0)
    
    open = []
    closed = {}

    heappush(open, start_node)
    
    while open:
        min_node = heappop(open)
        
        if min_node.key() in closed.keys():
            continue
        
        closed[min_node.key()] = min_node

        for step in generate_steps(grid, min_node):            
            if step.key() not in closed.keys() or step.heat_loss_acc < closed[step.key()].heat_loss_acc:                
                heappush(open, step)        
    
    return closed

grid = [[int(char) for char in line.strip()] for line in fileinput.input()]

start = (0, 0)
goal = (len(grid[0]) - 1, len(grid) - 1)

closed = search(grid, start)

minimum = sys.maxsize
for key, node in closed.items():
    if key[0] == goal:
        minimum = min(minimum, node.heat_loss_acc)

print(minimum)
