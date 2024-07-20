import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
-4 3
2 1
3 4


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
ans = False

# vector
v1 = [x2 - x1, y2 - y1]
v2 = [x3 - x2, y3 - y2]
v3 = [x1 - x3, y1 - y3]


# inner product
def inner_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


if (
    inner_product(v1, v2) == 0
    or inner_product(v1, v3) == 0
    or inner_product(v2, v3) == 0
):
    ans = True

print("Yes" if ans else "No")
