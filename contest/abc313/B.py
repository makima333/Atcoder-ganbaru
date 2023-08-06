import io
from operator import mod
import sys

_INPUT = """\
4
4 7 3 7

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
n, m = map(int, input().split())

winner = set([])
looser = set([])

for _ in range(m):
    a, b = map(int, input().split())
    winner.add(a)
    looser.add(b)


ans = winner - looser

if len(ans) != 1:
    print(-1)
else:
    print(*ans)
