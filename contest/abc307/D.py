import io
from operator import mod
import sys

_INPUT = """\
8
a(b(d))c



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
S = input()
ans = []
open_stack = []


for c_i, c in enumerate(list(S)):
    if c not in ["(", ")"]:
        ans.append(c)
    elif c == "(":
        ans.append(c)
        open_stack.append(c_i)
    elif c == ")":
        if len(open_stack) == 0:
            ans.append(c)
        else:
            x = open_stack.pop()
            while ans[-1] != "(":
                ans.pop()
            ans.pop()

print("".join(ans))
