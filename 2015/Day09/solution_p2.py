import sys
import itertools
import fileinput

def add_connection(city1, city2, distance):
    if city1 not in graph:
        graph[city1] = {}

    graph[city1].update({city2: distance})

    if city2 not in graph:
        graph[city2] = {}

    graph[city2].update({city1: distance})

graph = {}

for line in fileinput.input():
    temp = line.strip().split(" ")
    city1 = temp[0]
    city2 = temp[2]
    distance = int(temp[4])

    add_connection(city1, city2, distance)

max = 0
for path in itertools.permutations(graph):
    acc = 0
    for i in range(len(path) - 1):
        acc += graph[path[i]][path[i+1]]

    if acc > max:
        max = acc
    
print(max)
