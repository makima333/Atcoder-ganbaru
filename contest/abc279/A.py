import io
from operator import mod
import sys

_INPUT = """\
vvwvw



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
ans = 0
for c in list(input()):
    if c == "v":
        ans += 1

    elif c == "w":
        ans += 2

print(ans)
