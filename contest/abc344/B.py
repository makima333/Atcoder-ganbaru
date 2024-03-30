import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
2
1
0
"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

ans = []
while True:
    try:
        ans.append(input())
    except:
        break

for a in reversed(ans):
    print(a)
