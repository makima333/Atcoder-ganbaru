import io
from operator import mod
import sys

_INPUT = """\
1 10
..........


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
h, w = map(int, input().split())
cnt = 0
for _ in range(h):
    row = input()
    for r in row:
        if r == "#":
            cnt += 1
print(cnt)
