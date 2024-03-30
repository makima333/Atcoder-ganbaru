import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
1 2 3
2
2 4
6
1 2 4 8 16 32
4
1 5 10 50

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
L = int(input())
C = set(map(int, input().split()))

can_cals = set()
for a in A:
    for b in B:
        for c in C:
            can_cals.add(a + b + c)

Q = int(input())
X = list(map(int, input().split()))
for x in X:

    if x in can_cals:
        print("Yes")
    else:
        print("No")
