import fileinput
import re
import math

input = fileinput.input()
lr_sqeunce = input.readline().strip()

graph = {}

input.readline()
for line in input:
    node, left, right = re.findall(r"[A-Z1-9]+", line)
    graph[node] = (left, right)

acc = 0
nodes = list(filter(lambda a: a.endswith("A"), list(graph.keys())))
steps = []
finished_nodes = [False] * len(nodes)
finished = False

while not finished:
    for step in lr_sqeunce:
        acc += 1
        for i in range(len(nodes)):
            if step == "L":
                nodes[i] = graph[nodes[i]][0]
            else:
                nodes[i] = graph[nodes[i]][1]

            if nodes[i].endswith("Z") and not finished_nodes[i]:
                finished_nodes[i] = True
                steps.append(acc)
        
        if all(finished_nodes):
            finished = True
            break

print(math.lcm(*steps))