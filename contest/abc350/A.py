import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
ABC000



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
S = input()
num = int(S[-3:])

ans = True

if num > 349 or num == 316 or num == 0:
    ans = False

print("Yes" if ans else "No")
