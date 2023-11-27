import fileinput

length = 0

for line in fileinput.input():    
    sizes = line.strip().split("x")
    sizes = [int(i) for i in sizes]
    sizes.sort()

    length += 2 * sizes[0] + 2 * sizes[1] + sizes[0] * sizes[1] * sizes[2]

print(length)