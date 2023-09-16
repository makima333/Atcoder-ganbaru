import io
from operator import mod


_INPUT = """\
3 2
2 3 2 1
2 3 2 1


"""
import sys

sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
import sys
from collections import defaultdict

# 再帰用
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
points = defaultdict(list)

for _ in range(M):
    a, b, x, y = map(int, input().split())
    points[a - 1].append((b - 1, x, y))
    points[b - 1].append((a - 1, -x, -y))

ans = [[0, 0]]
ans += ["undecidable" for _ in range(N - 1)]
history = set()


def dfs(p, x, y):
    for tmp_p, tmp_x, tmp_y in points[p]:
        if tmp_p not in history:
            ans[tmp_p] = [x + tmp_x, y + tmp_y]
            history.add(tmp_p)
            dfs(tmp_p, x + tmp_x, y + tmp_y)


dfs(0, 0, 0)
for a in ans:
    if "undecidable" == a:
        print("undecidable")
    else:
        print(*a)
