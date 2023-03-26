import io
from operator import mod
import sys

_INPUT = """\
10
295 2 29 295 29 2 29 295 2 29


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

ss = map(int, input().split())

import collections

ans = 0
for k, v in collections.Counter(ss).items():
    ans += v // 2

print(ans)
