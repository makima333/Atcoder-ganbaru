import io
from operator import mod

_INPUT = """\
5 4
4 2
3 1
5 2
3 2



"""
import sys

sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import sys

sys.setrecursionlimit(1000000000)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

clr = [-1 for _ in range(n)]
cvs = [0 for _ in range(2)]


def c2(num):
    return num * (num - 1) // 2


def dfs(v, nc=0):
    if clr[v] != -1:
        return clr[v] == nc
    clr[v] = nc
    cvs[nc] += 1
    for u in g[v]:
        if nc == 0:
            if not dfs(u, 1):
                return False
        else:
            if not dfs(u, 0):
                return False

    return True


ans = c2(n) - m

for i in range(n):
    if clr[i] != -1:
        continue
    cvs = [0 for _ in range(2)]
    if not dfs(i):
        print(0)
        exit()
    for s in cvs:
        ans -= c2(s)

print(ans)
