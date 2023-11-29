from __future__ import print_function
from itertools import groupby

output = "1113122113"

for i in range(50):    
    output = "".join([str(len(list(iter))) + number for number, iter in groupby(output)])
        
print(len(output))