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

N = int(input())

nb = bin(N)[2:]

cnt = 0
for s in list(str(nb)):
    if s == "0":
        cnt += 1
    else:
        cnt = 0


print(cnt)
