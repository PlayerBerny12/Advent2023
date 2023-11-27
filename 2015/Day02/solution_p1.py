import fileinput

surface = 0

for line in fileinput.input():
    sizes = line.strip().split("x")
    sizes = [int(i) for i in sizes]
    sizes.sort()

    surface += 2 * sizes[0] * sizes[1] + 2 * sizes[1] * sizes[2] + 2 * sizes[0] * sizes[2] + sizes[0] * sizes[1]

print(surface)