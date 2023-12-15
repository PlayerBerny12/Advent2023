import fileinput

def hash(word):
    value = 0
    
    for char in word:
        value += ord(char)
        value *= 17
        value = value % 256
    
    return value

input = fileinput.input().readline().strip().split(",")

acc = 0
for word in input:
    acc += hash(word)

print(acc)