import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
-20


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

X = int(input())


x = X // 10
if X % 10 == 0:
    pass
else:
    x += 1


print(x)
