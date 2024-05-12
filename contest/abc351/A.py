import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 2


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


t = list(map(int, input().split()))
a = list(map(int, input().split()))

print(sum(t) - sum(a) + 1)
