import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
commencement

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

from collections import Counter

S = list(input())
c = Counter(S)
cmax = c.most_common()[0][1]
cnt = [[] for _ in range(cmax)]

for cn in c:
    cnt[c[cn] - 1].append(cn)

ans = True
for cnt_item in cnt:
    if len(cnt_item) != 2 and len(cnt_item) != 0:
        ans = False
        break

print("Yes" if ans else "No")
