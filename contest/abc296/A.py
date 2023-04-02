import io
from operator import mod
import sys

_INPUT = """\
9
FMFMMFMFM

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
_ = input()
cc = list(input())
tmp = cc.pop(0)

for c in cc:

    if c == "F" and tmp == "M":
        tmp = c
    elif c == "M" and tmp == "F":
        tmp = c
    else:
        print("No")
        exit()
print("Yes")
