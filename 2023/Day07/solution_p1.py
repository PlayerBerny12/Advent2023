import fileinput
from collections import Counter

order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def get_order(game):
    type = game[0]
    hand = game[1]

    return type, (order.index(hand[0]) + 1) * 100000000 + (order.index(hand[1]) + 1) * 1000000 + \
        order.index(hand[2]) * 10000 + order.index(hand[3]) * 100 + order.index(hand[4])

games = []

for line in fileinput.input():
    hand, bid = line.strip().split(" ")    
    counts = Counter(hand)
    most_common = counts.most_common(2)

    if most_common[0][1] == 5:
        games.append((6, hand, bid))
    elif most_common[0][1] == 4:
        games.append((5, hand, bid))
    elif most_common[0][1] == 3 and most_common[1][1] == 2:
        games.append((4, hand, bid))
    elif most_common[0][1] == 3:
        games.append((3, hand, bid))
    elif most_common[0][1] == 2 and most_common[1][1] == 2:
        games.append((2, hand, bid))
    elif most_common[0][1] == 2:
        games.append((1, hand, bid))
    else:
        games.append((0, hand, bid))
    
games.sort(key=get_order)

acc = 0
for i in range(len(games)):
    acc += int(games[i][2]) * (i + 1) 
print(acc)