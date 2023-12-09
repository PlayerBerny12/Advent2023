import fileinput
import re

def next_element(sequence):
    sequence_diff = [int(j)-int(i) for i,j in zip(sequence, sequence[1:])]

    if all(k == 0 for k in sequence_diff):
        return sequence[-1]
    else:        
        return int(sequence[-1]) + next_element(sequence_diff)

acc = 0
for line in fileinput.input():
    sequence = re.findall(r"-?\d+", line)
    next = next_element(sequence)
    acc += int(next)
    
print(acc)