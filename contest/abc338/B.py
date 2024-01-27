import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
pseudopseudohypoparathyroidism



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

S = list(input())

from collections import Counter

c = Counter(S)

ans = []
max_cnt = c.most_common()[0][1]

for k, v in c.most_common():
    if v == max_cnt:
        ans.append(k)

ans.sort()
print(ans[0])
