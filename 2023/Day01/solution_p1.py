import fileinput

acc = 0
for line in fileinput.input():
    values = []
    for char in line:
        try:
            values.append(int(char))
        except:
            ...

    acc += int(f"{values[0]}{values[-1]}")

print(acc)