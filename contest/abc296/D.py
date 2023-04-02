import io
from operator import mod
import sys

_INPUT = """\
2 5




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import math

n, m = map(int, input().split())
ans = 10**18
for a in range(1, min(n, math.ceil(m ** (1 / 2))) + 1):
    b = math.ceil(m / a)
    if b <= n:
        ans = min(ans, a * b)

if ans == 10**18:
    print(-1)
    exit()

print(ans)
