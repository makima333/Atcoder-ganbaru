import io
from operator import mod
import sys

_INPUT = """\
4
4 10
3 2
2 4
4 12

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
from collections import defaultdict

ice = defaultdict(list)

for _ in range(N):
    f, s = map(int, input().split())
    ice[f].append(s)

ans = []
max_flavor = []
for f in ice:
    ice[f].sort(reverse=True)

    if len(ice[f]) > 1:
        ans.append(ice[f][0] + ice[f][1] // 2)
    max_flavor.append(ice[f][0])

max_flavor.sort(reverse=True)
if len(max_flavor) > 1:
    ans.append(max_flavor[0] + max_flavor[1])
print(max(ans))
