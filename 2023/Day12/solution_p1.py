import fileinput
from  itertools import groupby

def generate_patterns(original_pattern):
    patterns_chars = []
    unknowns = [i for i, char in enumerate(original_pattern) if char == "?"]
    unknowns_length = len(unknowns)
    
    for i in range(2 ** unknowns_length):
        score = i
        pattern_chars = ["#"] * unknowns_length
        for j in range(unknowns_length, 0, -1):
            j -= 1

            if 2 ** j <= score:
                pattern_chars[j] = "."
                score -= 2 ** j

        patterns_chars.append(pattern_chars)
    
    patterns = []
    for pattern in patterns_chars:
        new_pattern = original_pattern

        for index, unknown in enumerate(unknowns):
            new_pattern = new_pattern[:unknown] + pattern[index] + new_pattern[unknown + 1:]

        patterns.append(new_pattern)
    
    return patterns

acc = 0
for line in fileinput.input():
    original_pattern, groups = line.strip().split(" ")
    groups = list(map(int, groups.split(",")))
    patterns = generate_patterns(original_pattern)
    
    for pattern in patterns:
        hash_counts = []
        
        for letter, repeats in groupby(pattern):
            if letter == "#":
                hash_counts.append(len(list(repeats)))
        if hash_counts == groups:
            acc += 1

print(acc)

