import io
from operator import mod
import sys

_INPUT = """\
6 -4
-2 -7 -1 -8 -2 -8




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, x = map(int, input().split())
aa = set(list(map(int, input().split())))


bb = set([])

for a in aa:
    bb.add(a + x)


if len(aa | bb) == len(aa) * 2:
    print("No")

else:
    print("Yes")
