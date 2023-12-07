import fileinput
from collections import Counter

order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def get_order(game):
    type = game[0]
    hand = game[1]

    return type, (order.index(hand[0]) + 1) * 100000000 + (order.index(hand[1]) + 1) * 1000000 + \
        order.index(hand[2]) * 10000 + order.index(hand[3]) * 100 + order.index(hand[4])

games = []

for line in fileinput.input():
    hand, bid = line.strip().split(" ")    
    max_hand = None
    max_type = 0

    for char in order:
        if char == "J":
            continue

        temp_hand = hand.replace("J", char)        
        counts = Counter(temp_hand)
        most_common = counts.most_common(2)  

        if most_common[0][1] == 5 and max_type <= 6:
            max_hand = (hand, bid)
            max_type = 6
            break
        elif most_common[0][1] == 4 and max_type <= 5:
            max_hand = (hand, bid)
            max_type = 5
        elif most_common[0][1] == 3 and most_common[1][1] == 2 and max_type <= 4:
            max_hand = (hand, bid)
            max_type = 4
        elif most_common[0][1] == 3 and max_type <= 3:
            max_hand = (hand, bid)
            max_type = 3
        elif most_common[0][1] == 2 and most_common[1][1] == 2 and max_type <= 2:
            max_hand = (hand, bid)
            max_type = 2
        elif most_common[0][1] == 2 and max_type <= 1:
            max_hand = (hand, bid)
            max_type = 1
        elif  max_type == 0:
            max_hand = (hand, bid)      
            max_type = 0

    games.append((max_type, max_hand[0], max_hand[1]))
    
games.sort(key=get_order)

acc = 0
for i in range(len(games)):
    acc += int(games[i][2]) * (i + 1) 
print(acc)
