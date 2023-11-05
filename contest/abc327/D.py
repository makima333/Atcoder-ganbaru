import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 2
1 2
2 3



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
n, m = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


ss = set([])
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
for a, b in zip(aa, bb):
    if (b, a) not in ss:
        ss.add((a, b))

uf = UnionFind((n + 1) * 2)
for a, b in ss:
    uf.union(a, b + n)
    uf.union(a + n, b)

for a, b in ss:
    if uf.same(a, b):
        print("No")
        exit()
print("Yes")
