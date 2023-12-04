import sys
import re
from itertools import islice 
  
def chunk(arr_range, arr_size): 
    arr_range = iter(arr_range) 
    return iter(lambda: tuple(islice(arr_range, arr_size)), ()) 

cards = {}
for i in range(1, 214):
    cards[i] = 1

for game in chunk(re.findall(r"\d+", sys.stdin.read()), 36):
    game_id = int(game[0])
    same_numbers = set(game[1:11]).intersection(game[11:])

    try:
        for i in range(game_id + 1, game_id + len(same_numbers) + 1):
            cards[i] += cards[game_id]
    except:
        ...

print(sum(cards.values()))