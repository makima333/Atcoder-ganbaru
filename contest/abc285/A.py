import io
from operator import mod
import sys

_INPUT = """\
1 2


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

if a + a == b or a + a + 1 == b:
    print("Yes")
else:

    print("No")
