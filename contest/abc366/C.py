import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
8
1 2
1 2
3
2 2
1 4
1 4
2 2
3


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
from collections import defaultdict

bag = defaultdict(int)

N = int(input())

for _ in range(N):
    s = input()
    if len(s) == 1:
        q = int(s)
    else:
        q, x = map(int, s.split())
    if q == 1:
        bag[x] += 1
    elif q == 2:
        bag[x] -= 1
        if bag[x] == 0:
            bag.pop(x)
    else:
        print(len(bag.keys()))
