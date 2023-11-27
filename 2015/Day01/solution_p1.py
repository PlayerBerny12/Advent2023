import fileinput

line = fileinput.input().readline()

floor = 0
for char in line:
    if char == '(':
        floor += 1
    else:
        floor -= 1
    
print(floor)