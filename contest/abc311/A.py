import io
from operator import mod
import sys

_INPUT = """\
5
ACABB

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ss = input()
ans = set([])

for s_i, s in enumerate(list(ss)):
    ans.add(s)
    if len(ans) == 3:
        print(s_i+1)
        exit()