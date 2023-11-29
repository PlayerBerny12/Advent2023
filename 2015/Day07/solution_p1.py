import sys
import re
from enum import Enum

class Operator(str, Enum):
    AND = "AND"
    OR = "OR"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"

def get_formula(formula):
    if formula[0] == "" and formula[1] == "" and formula[2] == "":
        return (formula[3], formula[4], formula[5], formula[6])
    else:
        return (formula[0], formula[1], formula[2])

def get_value(variable):
    try:
        return int(variable)
    except:    
        return known_variables.get(variable)

known_variables = {}
formulas = re.findall(r"(NOT\s)?(\w+|\d+)\s->\s(\w+)|(\w+|\d+)\s(AND|OR|LSHIFT|RSHIFT)\s(\w+|\d+)\s->\s(\w+)", sys.stdin.read())

while known_variables.get("a") == None:
    for formula in formulas:
        formula = get_formula(formula)
        
        if len(formula) == 3:
            result = get_value(formula[2])
            var = get_value(formula[1])

            if result == None and var != None:            
                if formula[0] == "":
                    known_variables[formula[2]] = var
                else:
                    known_variables[formula[2]] = ~var
        else:   
            result = get_value(formula[3])
            var1 = get_value(formula[0])
            var2 = get_value(formula[2])

            if result == None and var1 != None and var2 != None:            
                if formula[1] == Operator.AND:
                    known_variables[formula[3]] = var1 & var2
                elif formula[1] == Operator.OR:
                    known_variables[formula[3]] = var1 | var2
                elif formula[1] == Operator.LSHIFT:
                    known_variables[formula[3]] = var1 << var2
                elif formula[1] == Operator.RSHIFT:
                    known_variables[formula[3]] = var1 >> var2

print(known_variables["a"])