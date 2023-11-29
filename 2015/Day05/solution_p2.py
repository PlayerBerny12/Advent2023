import fileinput

nice_count = 0

for line in fileinput.input():    
    double_letter = False    
    previous_chars = ["", ""]
    
    for char in line:
        if previous_chars[1] == char:
            double_letter = True
        
        previous_chars[1] = previous_chars[0]
        previous_chars[0] = char

        
    for i in range(len(line) - 1):
        double_char = line[i:i+2]
        pair_count = 0

        iterator = iter(range(len(line) - 1))
        for j in iterator:
            if line[j:j+2] == double_char:
                pair_count += 1                
                next(iterator, None)

        if pair_count >= 2:
            break

    if double_letter and pair_count >= 2:
            nice_count += 1

print(nice_count)