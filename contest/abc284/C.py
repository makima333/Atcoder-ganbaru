import io
from operator import mod
import sys

_INPUT = """\
5 3
1 2
1 3
4 5



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())
ans = 0
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(num):
    visited[num] = True
    for visit_n in graph[num]:
        if not visited[visit_n]:
            dfs(visit_n)


for i in range(1, n + 1):
    if visited[i]:
        continue
    ans += 1
    dfs(i)

print(ans)
