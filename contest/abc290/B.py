import io
from operator import mod
import sys

_INPUT = """\
10 3
oxxoxooxox





"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())
ss = list(input())


ans = []
for s in ss:
    if m > 0:
        if s == "o":
            m -= 1
            ans.append(s)
        else:
            ans.append(s)
    else:
        ans.append("x")


print("".join(ans))
