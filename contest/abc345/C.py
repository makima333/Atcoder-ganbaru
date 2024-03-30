import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
aaaaa


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------\
S = list(input())

from collections import Counter

c = Counter(S)
total = len(S)
ans = 0

for s in S:
    s_cnt = c[s]
    ans += total - s_cnt
    total -= 1
    c[s] -= 1

if len(S) == len(set(S)):
    print(ans)
else:
    print(ans + 1)
