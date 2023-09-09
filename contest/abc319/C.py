import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
7 7 6
8 6 8
7 7 6

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

import itertools

ll = []
for _ in range(3):
    ll += map(int, input().split())
cand = [
    # 横一列ずつ
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    # 縦一列ずつ
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    # ななめ
    (0, 4, 8),
    (2, 4, 6),
]


def check(p):
    # print(p)
    for a, b, c in cand:
        for _ in range(3):
            if ll[a] == ll[b] and p[a] < p[c] and p[b] < p[c]:
                return False
            a, b, c = b, c, a
    return True


print(sum(check(p) for p in list(itertools.permutations(range(9)))) / 362880)
