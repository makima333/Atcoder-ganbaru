import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
0.100


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = float(input())

ans = str(N)
print(ans if not ans.endswith(".0") else str(N)[:-2])
