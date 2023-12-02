import re

Z = "z"

def change_char(input, index, char):
    return input[:index] + char + input[index + 1:]

def add_one_char(input):
    return chr(ord(input) + 1)

def add_one_string(input):
    length = len(input)    
    index = length - 1
    
    if input[index] == Z:
        input = change_char(input, index, "a")        

        for i in range(index):
            index = length - i - 2            

            if input[index] == Z:
                input = change_char(input, index, "a")
                overflow = True
            else:
                input = change_char(input, index, add_one_char(input[index]))
                overflow = False
                break                
        
        if overflow:
            input = "a" + input
    else:        
        input = change_char(input, index, add_one_char(input[index]))

    return input

def validate(input):    
    if "i" in input or "o" in input or "l" in input:
        return False
    
    if len(re.findall(r"([a-z])\1.*([a-z])\2", input)) == 0:
        return False
    
    for i in range(len(input) - 3):
        if ord(input[i]) + 2 == ord(input[i+1]) + 1 == ord(input[i+2]):
            return True
    
    return False

input = "vzbxkgha"
while True:
    input = add_one_string(input)
    
    if validate(input):
        break
print(input)