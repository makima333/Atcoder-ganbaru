import io
from operator import mod
import sys

_INPUT = """\
hjklo;jil


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = input()
a_i = 0
if "a" in n:
    for i, c in enumerate(list(n)):
        if c == "a":
            a_i = i + 1
    print(a_i)

else:
    print(-1)
