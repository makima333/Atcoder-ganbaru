import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6
4 1 -1 5 3 2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
A = list(map(int, input().split()))

dest = [0 for _ in range(N + 1)]

for a_i, a in enumerate(A):
    if a == -1:
        head = a_i
    else:
        dest[a] = a_i

ans = [head + 1]

for _ in range(N - 1):
    ans.append(dest[ans[-1]] + 1)

print(*ans)
