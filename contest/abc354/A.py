import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


H = int(input())
p = 0
ans = 0
while H > p:
    ans += 1
    p += 2**ans

print(ans + 1)
