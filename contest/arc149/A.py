import io
from operator import mod
import sys

_INPUT = """\
9 12


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

n, m = map(int, input().split())

max_mem = [0, 0]

for i in range(1, 10):
    tmp = 0
    for j in range(1, n + 1):
        tmp = tmp * 10 + i
        tmp %= m
        if tmp == 0:
            max_mem = max(max_mem, [j, i])

if max_mem[0] != 0:
    print(str(max_mem[1]) * max_mem[0])
else:
    print(-1)
