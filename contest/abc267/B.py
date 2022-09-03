import io
import sys
from tokenize import Double

_INPUT = """\
0000000000

 
"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
pins = list(input())
pins = [int(i) for i in pins]

if pins[0] == 1:
    print("No")
    exit()
else:
    cols = []
    cols.append(sum([pins[6]]))
    cols.append(sum([pins[3]]))
    cols.append(sum([pins[1], pins[7]]))
    cols.append(sum([pins[0], pins[4]]))
    cols.append(sum([pins[2], pins[8]]))
    cols.append(sum([pins[5]]))
    cols.append(sum([pins[9]]))
    split = []
    empty_col  = []
    for i, col_sum in enumerate( cols):
        if col_sum == 0:
            if i !=0 and i != len(cols)-1:
                empty_col.append(i)
        else:
            split.append(i)
    
    try:
        left = min(split)
        right = max(split)
    except ValueError:
        print("No")
        exit()

    for col in empty_col:
        if left < col and col < right:
            print("Yes")
            exit()
    

    print("No")
    exit()

            
