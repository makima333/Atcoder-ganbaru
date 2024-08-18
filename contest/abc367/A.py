import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
0 21 7


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
A, B, C = map(int, input().split())

sleep = set()

while True:
    sleep.add(B)

    if B == C:
        break

    if B == 23:
        for c in range(C + 1):
            sleep.add(c)
        break

    B += 1

if A not in sleep:
    print("Yes")
else:
    print("No")
