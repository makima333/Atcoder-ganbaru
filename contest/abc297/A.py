import io
from operator import mod
import sys

_INPUT = """\
4 500
100 

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, d = map(int, input().split())

tt = list(map(int, input().split()))

x1 = 0
for t_i, t in enumerate(tt):
    if t_i == 0:
        x1 = t
        continue

    x2 = t
    # print(x1, x2)
    if x2 - x1 <= d:
        print(t)
        exit()
    else:
        x1 = t

print(-1)
