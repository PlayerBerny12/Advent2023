import fileinput

line = fileinput.input().readline()

grid = [[0 for _ in range(len(line))] for _ in range(len(line))]
x = 0
y = 0
grid[x][y] = 1

for char in line:
    if char == '^':
        x += 1
    elif char == 'v':
        x -= 1
    elif char == '<':
        y -= 1
    elif char == '>':
        y += 1

    grid[x][y] += 1

count = 0
for line in grid:
    for cell in line:
        if cell > 0:
            count += 1

print(count)