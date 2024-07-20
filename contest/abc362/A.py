import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
20 30 10
Blue
    

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
R, G, B = map(int, input().split())
C = input()

if C == "Red":
    ans = [G, B]
elif C == "Green":
    ans = [R, B]
else:
    ans = [R, G]

print(min(ans))
