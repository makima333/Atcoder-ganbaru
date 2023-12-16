import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
9
1 2
2 3
2 4
2 5
1 6
6 7
7 8
7 9


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
import sys

sys.setrecursionlimit(10**6)

N = int(input())

uv = [set() for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    uv[u - 1].add(v - 1)
    uv[v - 1].add(u - 1)


def dfs(j, his_set):
    his_set.add(j)
    # print(his_set)
    for k in uv[j]:
        if k not in his_set:
            dfs(k, his_set)


tl = []
if len(uv[0]) == 1:
    print(1)
    exit()

# print(uv)
for i in uv[0]:
    tmp = set([0])
    dfs(i, tmp)
    # print(tmp)
    tl.append(len(tmp) - 1)

tl.sort()
print(sum(tl[:-1]) + 1)
