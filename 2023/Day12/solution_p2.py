import os
import fileinput
from multiprocessing import Pool
from functools import cache

@cache
def process_patter(pattern, groups, temp):
    if len(groups) == 0:
        if "#" in pattern:
            return 0
        else:
            return 1 
    
    if len(pattern) == 0:
        if len(groups) == 1 and temp == groups[0]:
            return 1
        else:
            return 0
    
    if pattern[0] == ".":
        if temp == 0:
            return process_patter(pattern[1:], groups, 0)    
        elif temp == groups[0]:
            return process_patter(pattern[1:], groups[1:], 0)    
        else:
            return 0
    
    if pattern[0] == "?":
        return process_patter(f".{pattern[1:]}", groups, temp) \
            + process_patter(f"#{pattern[1:]}", groups, temp)
    else:
        if temp > groups[0]:
            return 0
        else:
            return process_patter(pattern[1:], groups, temp + 1)

def task(line):
    original_pattern, groups = line.strip().split(" ")
    
    groups = tuple(map(int, groups.split(","))) * 5
    pattern = "?".join([original_pattern] * 5)
    return process_patter(pattern, groups, 0)

pool = Pool(os.cpu_count()-1)     
print(sum(pool.map(task, fileinput.input())))
