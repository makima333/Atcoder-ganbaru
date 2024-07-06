import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
0 0 0 1000 1000 1000
10 10 10 100 100 100



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, m = map(int, input().split())

a_v = (d - a) * (e - b) * (f - c)
b_v = (j - g) * (k - h) * (m - i)

ans = False
if a_v >= b_v:
    x, y, z = g, h, i
    while x <= j:
        dy = y
        while dy <= k:
            dz = z
            while dz <= m:
                # print(x, dy, dz)
                if a < x < d and b < dy < e and c < dz < f:
                    ans = True
                    break
                dz += 1
            dy += 1
        x += 1
else:
    x, y, z = a, b, c
    while x <= d:
        dy = y
        while dy <= e:
            dz = z
            while dz <= f:
                # print(x, dy, dz)
                if g < x < j and h < dy < k and i < dz < m:
                    ans = True
                    break
                dz += 1
            dy += 1
        x += 1

if a == g and b == h and c == i and d == j and e == k and f == m:
    ans = True

print("Yes" if ans else "No")
