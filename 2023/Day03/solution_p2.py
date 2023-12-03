import fileinput

def add_gear(x, y, number):
    global gears

    if gears.get(f"{x},{y}") == None:
        gears[f"{x},{y}"] = [number]
    else:
        gears[f"{x},{y}"].append(number)

def find_symbol(x, y, length, number):
    global grid

    try:
        if grid[y][x] == "*":
            add_gear(x, y, number)                        
        if grid[y][x - length - 1] == "*":
            add_gear(x - length - 1, y, number)                        
    except:
        ...

    for i in range(x - length - 1, x + 1):
        try:
            if grid[y-1][i] == "*":      
                add_gear(i, y-1, number)                  
            
            if grid[y+1][i] == "*":
                add_gear(i, y+1, number)                            
        except:
            ...    

grid = []
gears = {}

for line in fileinput.input():
    grid.append([])
    for char in line.strip():
        grid[-1].append(char)
 
for y in range(len(grid)):
    number_string = ""    

    for x in range(len(grid[y])):        
        if grid[y][x].isdigit():
            number_string += grid[y][x] 
        else:
            if number_string != "":
                number = int(number_string)
                length = len(number_string)
                number_string = ""                

                find_symbol(x, y, length, number)  

    if number_string != "":
        number = int(number_string)
        length = len(number_string)
        number_string = ""                
        
        find_symbol(x, y, length, number)
        
acc = 0
for key, value in gears.items(): 
    if len(value) == 2:
        acc += value[0] * value[1]

print(acc)
    