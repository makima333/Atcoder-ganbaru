import io
from operator import mod
import sys

_INPUT = """\
6
a
abc
de
cba
de
aba

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

bar = set([])
cnt = 0

for _ in range(n):
    tmp = input()
    tmp_r = tmp[::-1]
    
    if tmp < tmp_r:
        bar.add(tmp)
    else:
        bar.add(tmp_r)

print(len(bar)) 