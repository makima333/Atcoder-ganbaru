import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3 10 1
1 2 3


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, T, P = map(int, input().split())
L = list(map(int, input().split()))

L.sort(reverse=True)
L = L[:P]

if min(L) >= T:
    print(0)
    exit()

print(T - min(L))
