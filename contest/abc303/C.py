import io
from operator import mod
import sys

_INPUT = """\
4 2 3 1
RUDL
-1 -1
1 0


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

n, m, h, k = map(int, input().split())
actions = input()
import collections

items = collections.defaultdict(set)

for _ in range(m):
    x, y = map(int, input().split())
    items[x].add(y)

x, y = (0, 0)
cnt = 0
for act in list(actions):
    if act == "R":
        x = x + 1

    if act == "L":
        x = x - 1

    if act == "U":
        y = y + 1

    if act == "D":
        y = y - 1

    cnt += 1
    h -= 1
    if h < 0:
        break

    if h < k and y in items[x]:
        h = k
        items[x] = items[x] - set([y])

if h >= 0 and cnt == n:
    print("Yes")
else:
    print("No")
