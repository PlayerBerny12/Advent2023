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
    red_max = 0
    green_max = 0
    blue_max = 0
    
    for set in game.split(";"):
        for cube in set.split(","):
            count, color = cube.strip().split(" ")
            count = int(count)

            if color == Color.RED and red_max < count:
               red_max = count
            elif color == Color.GREEN and green_max < count:
               green_max = count
            elif color == Color.BLUE and blue_max < count:
                blue_max = count    
    
    acc += red_max * green_max * blue_max

print(acc)