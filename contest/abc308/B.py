import io
from operator import mod
import sys

_INPUT = """\
3 2
red green blue
blue red
800 1600 2800



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())

cc = list(input().split())
dd = list(input().split())
pp = list(map(int, input().split()))

not_in_c = pp.pop(0)
price_map = {}

for d_i, d in enumerate(dd):
    price_map[d] = pp[d_i]


dd_set = set(dd)

ans = 0
for c in cc:
    if c in dd_set:
        ans += price_map[c]
    else:
        ans += not_in_c

print(ans)
