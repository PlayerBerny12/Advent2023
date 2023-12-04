import sys
import re
from itertools import islice 
  
def chunk(arr_range, arr_size): 
    arr_range = iter(arr_range) 
    return iter(lambda: tuple(islice(arr_range, arr_size)), ()) 

def score(count):
    if count == 0:
        return 0

    score = 1
    for _ in range(count - 1):
        score = score * 2

    return score

acc = 0
for game in chunk(re.findall(r"\d+", sys.stdin.read()), 36):    
    same_numbers = set(game[1:11]).intersection(game[11:])
    acc += score(len(same_numbers))

print(acc)