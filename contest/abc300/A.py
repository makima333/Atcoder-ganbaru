import io
from operator import mod
import sys

_INPUT = """\
1 1 1
2


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, a, b = map(int, input().split())

cc = list(map(int, input().split()))

for i, c in enumerate(cc):
    if c == a + b:
        print(i + 1)
        exit()
