import io
from operator import mod
import sys

_INPUT = """\
7 6
5 R 3 R
7 R 4 R
4 B 1 R
2 R 3 B
2 B 5 B
1 B 7 B



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())


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


uf = UnionFind(n)
cycle = 0
for _ in range(m):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1

    if uf.same(a, c):
        cycle += 1
    else:
        uf.unite(a, c)

grouped = [[] for _ in range(n)]
for i in range(n):
    # if tmp != 0:
    grouped[uf.find(i)].append(i)

not_cycle = 0
for g in grouped:
    if g != []:
        not_cycle += 1

# print(grouped)
print(cycle, not_cycle - cycle)
