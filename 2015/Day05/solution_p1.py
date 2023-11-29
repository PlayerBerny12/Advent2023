import fileinput

nice_count = 0

for line in fileinput.input():
    vowel_count = 0
    double_letter = False
    previous_char = ""
    
    if "ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line:
        for char in line:
            if previous_char == char:
                double_letter = True
            
            previous_char = char

            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                vowel_count += 1

        if double_letter and vowel_count >= 3:
            nice_count += 1

print(nice_count)