import io
from operator import mod
import sys

_INPUT = """\
5
1 2 3 5 6




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

aa = list(map(int, input().split()))
ans = []
for a in aa:
    if a % 2 == 0:
        ans.append(str(a))

print(" ".join(ans))
