import io
from operator import mod
import sys

_INPUT = """\
3 4 6
1 2
2 3
4 5
4 6
1 3
6 7


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
# graph bfs
from collections import defaultdict, deque


n1, n2, m = map(int, input().split())

edge = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)


def bfs(edge, start):
    q = deque([start])
    dist = [-1 for i in range(n1 + n2 + 1)]
    dist[start] = 0
    while len(q) > 0:
        v = q.popleft()
        for nv in edge[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    return max(dist)


print(bfs(edge, 1) + bfs(edge, n1 + n2) + 1)
