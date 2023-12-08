import fileinput
import re

input = fileinput.input()
lr_sqeunce = input.readline().strip()

graph = {}

input.readline()
for line in input:
    node, left, right = re.findall(r"[A-Z]+", line)
    graph[node] = (left, right)

acc = 0
node = "AAA"
found = False

while not found:
    for step in lr_sqeunce:
        acc += 1
        
        if step == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        
        if node == "ZZZ":
            found = True
            break

print(acc)