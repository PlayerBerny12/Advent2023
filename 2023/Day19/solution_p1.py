import fileinput
import re

class Part():
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    
    def sum_ratings(self):
        return self.x + self.m + self.a + self.s

class Rule():
    def __init__(self, sections):
        self.sections = sections    
    
    def match(self, part):
        for section in self.sections[:-1]:
            section_rule, section_result = section.split(":")
            
            if section_rule[0] == "x":
                value = part.x    
            elif section_rule[0] == "m":
                value = part.m
            elif section_rule[0] == "a":
                value = part.a
            elif section_rule[0] == "s":
                value = part.s
            else:
                raise Exception("Unknown part")    
            
            if section_rule[1] == ">":
                if value > int(section_rule[2:]):
                    return section_result
            elif section_rule[1] == "<":
                if value < int(section_rule[2:]):
                    return section_result
            else:
                raise Exception("Unknown rule")
        
        return self.sections[-1]        

rules = {}
parts = []
processing_rules = True

for line in fileinput.input():
    line = line.strip()

    if line == "":
        processing_rules = False
        continue

    if processing_rules:
        rule, rule_body = re.findall(r"([a-z]+)\{(.+)\}", line)[0]
        sections = rule_body.split(",")
        rules[rule] = Rule(sections)
    else:        
        x, m, a, s = re.findall(r"\d+", line)
        parts.append(Part(int(x), int(m), int(a), int(s)))

acc = 0
for part in parts:
    rule = "in"

    while rule != "A" and rule != "R":
        rule = rules[rule].match(part)

    if rule == "A":
        acc += part.sum_ratings()

print(acc)