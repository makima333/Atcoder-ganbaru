import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
6
salty
sweet
sweet
salty
sweet
sweet



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())

before = ""
for i in range(N):
    s = input()
    if s == "sweet" and before == "sweet" and i != N - 1:
        print("No")
        exit()
    before = s

print("Yes")
