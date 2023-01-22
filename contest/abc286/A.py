import io
from operator import mod
import sys

_INPUT = """\
10 2 4 7 9
22 75 26 45 72 81 47 29 97 2


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, p, q, r, s = map(int, input().split())
aa = list(map(int, input().split()))

import copy

ans = []
if p != 1:
    ans += aa[0 : p - 1]

ans += aa[r - 1 : s]

if q + 1 != r:
    ans += aa[q : r - 1]

ans += aa[p - 1 : q]

if n != s:
    ans += aa[s:]

print(*ans)
