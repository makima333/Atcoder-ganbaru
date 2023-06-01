import io
from operator import mod
import sys

_INPUT = """\
4
nok0
n0ko

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ss = input()
tt = input()

for i in range(n):
    s = ss[i]
    t = tt[i]
    if s != t:
        if (s in ["1", "l"] and t in ["1", "l"]) or (
            s in ["0", "o"] and t in ["0", "o"]
        ):
            pass
        else:
            print("No")
            exit()
print("Yes")
