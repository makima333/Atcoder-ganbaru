import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
4 3
1 2
2 3
1 4


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M = map(int, input().split())


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]


uf = UnionFind(N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    uf.unite(a, b)

root = {uf.find(i) for i in range(1, N + 1)}
total_edge = 0
for r in root:
    edge = uf.get_size(r) - 1
    total_edge += (edge * (edge + 1)) // 2

print(total_edge - M)
