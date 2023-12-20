import fileinput
import re
from copy import deepcopy

class Part_Combination():
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    
    def possible_combinations(self):
        return (self.x[1] - self.x[0] - 1) * (self.m[1] - self.m[0] - 1) * \
            (self.a[1] - self.a[0] - 1) * (self.s[1] - self.s[0] - 1)
    
    def shorten_interval(self, name, upper_bound, value_new):
        value = getattr(self, name)

        if upper_bound and value_new < value[1]:
            setattr(self, name, (value[0], value_new))
        elif not upper_bound and value_new > value[0]:
            setattr(self, name, (value_new, value[1]))

    def __repr__(self) -> str:
        return f"{self.x}, {self.m}, {self.a}, {self.s}"
    
class Rule():
    def __init__(self, sections):
        self.sections = sections
    
    def match(self, part_combination):
        part_combinations = []
        section_rules = []

        for section in self.sections[:-1]:
            section_rule, section_result = section.split(":")
            
            section_rules.append(section_rule)
            part_combinations.append((section_result, deepcopy(part_combination)))
        
        part_combinations.append((self.sections[-1], deepcopy(part_combination)))

        for i in range(len(section_rules)):
            section_rule = section_rules[i]

            if section_rule[1] == ">":
                upper_bound = False
            elif section_rule[1] == "<":
                upper_bound = True
            else:
                raise Exception("Unknown rule")

            value = int(section_rule[2:])
            
            for j in range(i, len(part_combinations)):
                if j == i:
                    part_combinations[j][1].shorten_interval(section_rule[0], upper_bound, value)
                else:
                    part_combinations[j][1].shorten_interval(section_rule[0], not upper_bound, value + 1 if not upper_bound else value - 1)

        return part_combinations

rules = {}
parts = []
processing_rules = True

for line in fileinput.input():
    line = line.strip()

    if line == "":
        break
    
    rule, rule_body = re.findall(r"([a-z]+)\{(.+)\}", line)[0]
    sections = rule_body.split(",")
    rules[rule] = Rule(sections)

    
accepted_part_combinations = []
open = [("in", Part_Combination((0, 4001), (0, 4001), (0, 4001), (0, 4001)))]

acc = 0
while len(open) > 0:    
    item = open[0]
    del open[0]
    
    if item[0] == "A":
        acc += item[1].possible_combinations()
    elif item[0] == "R":
        continue
    else:
        rule = rules[item[0]]
        open.extend(rule.match(item[1]))        

print(acc)