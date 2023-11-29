import fileinput

acc = 0
for line in fileinput.input():
    acc += len(line) - len(bytes(line, "utf-8").decode("unicode_escape")) + 2

print(acc)