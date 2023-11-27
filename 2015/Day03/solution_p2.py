import fileinput

line = fileinput.input().readline()

grid = [[0 for _ in range(len(line))] for _ in range(len(line))]
i = 0
x = [0,0]
y = [0,0]
grid[0][0] = 2

for char in line:
    if char == '^':
        x[i%2] += 1
    elif char == 'v':
        x[i%2] -= 1
    elif char == '<':
        y[i%2] -= 1
    elif char == '>':
        y[i%2] += 1

    grid[x[i%2]][y[i%2]] += 1
    i += 1

count = 0
for line in grid:
    for cell in line:
        if cell > 0:
            count += 1

print(count)