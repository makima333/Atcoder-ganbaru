import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1 0 0



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, T, A = map(int, input().split())

bigger = max(T, A)

if N // 2 < bigger:
    print("Yes")
else:
    print("No")
