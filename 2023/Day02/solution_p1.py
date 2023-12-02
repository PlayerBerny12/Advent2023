import sys
import re
from enum import Enum

class Color(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"    

lines = re.findall(r"Game\s(\d+):(.*)", sys.stdin.read())
acc = 0

for id, game in lines:
    possible = True

    for set in game.split(";"):
        for cube in set.split(","):
            count, color = cube.strip().split(" ")
            count = int(count)

            if color == Color.RED and count > 12 or \
               color == Color.GREEN and count > 13 or \
               color == Color.BLUE and count > 14:
                possible = False
        
    if possible:
        acc += int(id)

print(acc)
            
        