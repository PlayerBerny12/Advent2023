import fileinput

acc = 0
for line in fileinput.input():    
    acc += len(line.replace("\\", "\\\\").replace("\"", "\\\"")) - len(line) + 2 

print(acc)
    