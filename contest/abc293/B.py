import io
from operator import mod
import sys

_INPUT = """\
20
9 7 19 7 10 4 13 9 4 8 10 15 16 3 18 19 12 13 2 12



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

k = int(input())

xx = list(map(int, input().split()))

p = set([i for i in range(1, k + 1)])
his = set([])

for x_i, x in enumerate(xx):
    if x_i + 1 in his:
        continue
    else:
        his.add(x)


ans = list(p - his)

print(len(ans))
print(*ans)
