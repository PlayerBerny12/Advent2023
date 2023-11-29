output = "1113122113"

for i in range(40):
    input = output
    output = ""

    counter = 1
    previous_char = input[0]
    
    for char in input[1:]:
        if char == previous_char:
            counter += 1
            previous_char = char
        else:        
            output += f"{counter}{previous_char}"
            counter = 1
            previous_char = char

    output += f"{counter}{previous_char}"

print(len(output))