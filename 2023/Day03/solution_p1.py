import fileinput

def find_symbol(x, y, length, number):
    global acc, grid
    try:
        if (grid[y][x] != "." and not grid[y][x].isdigit()) or (grid[y][x - length - 1] != "." and not grid[y][x - length - 1].isdigit()):
            acc += number                        
            return
    except:
        ...

    for i in range(x - length - 1, x + 1):
        try:
            if (grid[y-1][i] != "." and not grid[y-1][i].isdigit()) or (grid[y+1][i] != "." and not grid[y+1][i].isdigit()):
                acc += number                            
                break                     
        except:
            ...              

acc = 0
grid = []

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
           
print(acc)  