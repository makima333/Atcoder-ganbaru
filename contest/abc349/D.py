import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 19


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

L, R = map(int, input().split())
ans = []
while L != R:
    i = 0
    while L % pow(2, i + 1) == 0 and L + pow(2, i + 1) <= R:
        i += 1
    ans.append([L, L + pow(2, i)])
    L += pow(2, i)

print(len(ans))
for a in ans:
    print(*a)
