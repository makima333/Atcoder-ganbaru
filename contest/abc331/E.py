import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
2 3 3
2 1
10 30 20
1 2
2 1
2 3

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M, L = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

ex = set()
for _ in range(L):
    c, d = map(int, input().split())
    ex.add((c - 1, d - 1))


bb_sorted = sorted(
    [(b_i, b) for b_i, b in enumerate(bb)], reverse=True, key=lambda x: x[1]
)
ans = -1
for a_i, a in enumerate(aa):
    for b_i, b in bb_sorted:
        if (a_i, b_i) not in ex:
            ans = max(ans, a + b)
            break

print(ans)
