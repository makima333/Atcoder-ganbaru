import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
CCCCCC

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

S = input()

abc = [0, 0, 0]

for s in S:
    if s == "A":
        if abc[1] > 0 or abc[2] > 0:
            print("No")
            exit()

        abc[0] += 1
    elif s == "B":
        if abc[2] > 0:
            print("No")
            exit()

        abc[1] += 1
    elif s == "C":
        abc[2] += 1

print("Yes")
