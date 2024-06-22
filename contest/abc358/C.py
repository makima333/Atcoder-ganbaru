import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 5
oooxx
xooox
xxooo

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, M = map(int, input().split())

all_p = {i for i in range(1, M + 1)}
pp = [set() for _ in range(N)]
for i in range(N):
    for s_i, s in enumerate(input()):
        if s == "o":
            pp[i].add(s_i + 1)

ans = []


def dfs(i, p, cnt):
    if i == N:
        # print(p)
        if len(p) == M:
            ans.append(cnt)
        return
    dfs(i + 1, p | pp[i], cnt + 1)
    dfs(i + 1, p, cnt)


dfs(0, set(), 0)

print(min(ans))
