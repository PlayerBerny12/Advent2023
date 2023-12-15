import fileinput

def hash(word):
    value = 0
    
    for char in word:
        value += ord(char)
        value *= 17
        value = value % 256
    
    return value

input = fileinput.input().readline().strip().split(",")

boxes = {}
for word in input:
    if word.endswith("-"):
        label = word[:-1]
        focal_length = None
    else:
        label, focal_length = word.split("=")
        focal_length = int(focal_length)

    box = hash(label)
    
    if box not in boxes:
        boxes[box] = []
        indexes = []
    else:
        indexes = [idx for idx, lens in enumerate(boxes[box]) if label == lens[0]]
        
    if focal_length != None:        
        if len(indexes) > 0:
            boxes[box][indexes[0]] = (label, focal_length)
        else:
            boxes[box].append((label, focal_length))
    else:
        if len(indexes) > 0:
            del boxes[box][indexes[0]]

acc = 0
for box in boxes: 
    for index, lens in enumerate(boxes[box]):
        acc += (box + 1) * (index + 1) * lens[1]
print(acc)