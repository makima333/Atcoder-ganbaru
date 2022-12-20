import io
from operator import mod
import sys

_INPUT = """\
20
a,"t,"c,"o,"d,"e,"r,


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
_ = input()
s = list(input())

flg = 0
ans = []
for c in s:
    if c == '"':
        flg += 1
    if flg % 2 == 0:
        if c == ",":
            ans.append(".")
        else:
            ans.append(c)
    else:
        ans.append(c)

print("".join(ans))
