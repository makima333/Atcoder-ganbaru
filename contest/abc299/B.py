import io
from operator import mod
import sys

_INPUT = """\
2 1000000000
1000000000 1
1 1000000000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

N, T = map(int, input().split())
cc = list(map(int, input().split()))
rr = list(map(int, input().split()))

if T not in set(cc):
    T = cc[0]

win = [0, 0]
for n_i in range(N):
    if cc[n_i] == T:
        if rr[n_i] > win[1]:
            win[0] = n_i
            win[1] = rr[n_i]


print(win[0] + 1)
