import io
from operator import mod
import sys

_INPUT = """\
8
national


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ss = input()

ans = []
for s_i, s in enumerate(ss):
    if s == "n":
        if s_i != len(ss) - 1 and ss[s_i + 1] == "a":
            ans.append(s)
            ans.append("y")
        else:
            ans.append(s)
    else:
        ans.append(s)

print("".join(ans))
