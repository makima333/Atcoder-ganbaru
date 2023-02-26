import io
from operator import mod
import sys

_INPUT = """\
10 3
oxxoxooxox



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
ans = 0
for b in bb:
    ans += aa[b - 1]

print(ans)
