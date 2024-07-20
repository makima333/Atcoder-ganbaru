import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 8
928448202 994752369 906965437 942744902 907560126
2 5 975090662
1 2 908843627
1 5 969061140
3 4 964249326
2 3 957690728
2 4 942986477
4 5 948404113
1 3 988716403


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

# ダイクストラ法, dicstra algorithm
N, M = map(int, input().split())
A = list(map(int, input().split()))

nodes = [10**18 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v, b = map(int, input().split())
    graph[u].append((v, b + A[v - 1]))
    graph[v].append((u, b + A[u - 1]))

nodes[1] = 0
import heapq

q = []
heapq.heappush(q, (0, 1))
while q:
    d, v = heapq.heappop(q)
    if d > nodes[v]:
        continue
    for u, w in graph[v]:
        if nodes[u] > nodes[v] + w:
            nodes[u] = nodes[v] + w
            heapq.heappush(q, (nodes[u], u))


nodes = [i + A[0] for i in nodes]
# print(graph)
print(*nodes[2:])
