import fileinput

line = fileinput.input().readline()

floor = 0
position = 0
for char in line:
    if char == "(":
        floor += 1
    else:
        floor -= 1

    position += 1

    if floor == -1:
        break

print(position)
