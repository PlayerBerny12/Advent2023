import fileinput

def get_string_number(input):    
    if input.startswith("one"):
        return 1
    elif input.startswith("two"):
        return 2
    elif input.startswith("three"):
        return 3
    elif input.startswith("four"):
        return 4
    elif input.startswith("five"):
        return 5
    elif input.startswith("six"):
        return 6
    elif input.startswith("seven"):
        return 7
    elif input.startswith("eight"):
        return 8
    elif input.startswith("nine"):
        return 9
    else:
        return None

acc = 0
for line in fileinput.input():
    values = []    

    for i in range(len(line)):        
        try:            
            values.append(int(line[i]))
        except:
           value = get_string_number(line[i:])

           if value != None:
                values.append(value)

    print(values)
    acc += int(f"{values[0]}{values[-1]}")

print(acc)