import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10
1000 10 9
1000 10 10
1000 10 2
1000 10 3
1000 10 4
1000 10 5
1000 10 6
1000 10 7
1000 10 8


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

# ダイクストラ法
N = int(input())

nodes = [10**18 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b, x = map(int, input().split())
    graph[i + 1].append((i + 2, a))
    graph[i + 1].append((x, b))

# print(graph)
nodes[1] = 0
import heapq

q = []
heapq.heappush(q, (0, 1))
while q:
    _, v = heapq.heappop(q)

    for u, w in graph[v]:
        if nodes[u] > nodes[v] + w:
            nodes[u] = nodes[v] + w
            heapq.heappush(q, (nodes[u], u))


print(nodes[-1])
# print(nodes)
