import io
from operator import mod
import sys

_INPUT = """\
6
2 7 1 8 2 8



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
from collections import *

n = int(input())
vols_l = list(map(int, input().split()))

sa = list(set(vols_l))
sa.sort(reverse=True)
a2 = Counter(vols_l)

for v in sa:
    print(a2[v])
for _ in range(n - len(sa)):
    print(0)
