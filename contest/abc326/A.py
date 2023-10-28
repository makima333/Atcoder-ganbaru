import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
99 96


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

x, y = map(int, input().split())

if y > x and (y - x) <= 2:
    print("Yes")
elif x > y and (x - y) <= 3:
    print("Yes")
else:
    print("No")
