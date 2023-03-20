import io
from operator import mod
import sys

_INPUT = """\
8 12
3 4 10 15 17 18 22 30
5 7 11 13 14 16 19 21 23 24 27 28



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())

aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

cc = aa + bb
cc.sort()

aa = set(aa)
bb = set(bb)


ans_a = []
ans_b = []
for i, c in enumerate(cc):
    if c in aa:
        ans_a.append(i + 1)
    else:
        ans_b.append(i + 1)

print(*ans_a)
print(*ans_b)
