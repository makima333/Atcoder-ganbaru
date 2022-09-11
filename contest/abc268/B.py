import io
import sys
from tokenize import Double

_INPUT = """\
atcodera
atcoder
 
"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n = list(input())
t = list(input())

if len(t) < len(n):
    print("No")
    exit()

for s_i, s in enumerate(n):
    if n[s_i] != t[s_i]:
        print("No")
        exit()

print("Yes")
    
    



            
