import io
from operator import mod
import sys

_INPUT = """\
6
3 2 3 4
2 3 5
0
1 5
0
0

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
import sys

sys.setrecursionlimit(10**9)

N = int(input())
books = {}
read_his = []
read_set = set()

for i in range(N):
    cp = list(map(int, input().split()))
    c = cp[0]
    if len(cp) > 0:
        books[i + 1] = cp[1:]
    else:
        books[i + 1] = []


def dfs(book):
    for b in books[book]:
        if b not in read_set:
            dfs(b)
    read_his.append(book)
    read_set.add(book)


dfs(1)
read_his.pop()
print(*read_his)
