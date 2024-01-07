import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 9
2 3
1 U
2 3
1 R
1 D
2 3
1 L
2 1
2 5

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, Q = map(int, input().split())
history = []

for _ in range(Q):
    a, b = input().split()

    if a == "1":
        if history:
            x, y = history[-1]
        else:
            x, y = 1, 0
        if b == "U":
            history.append((x, y + 1))
        elif b == "R":
            history.append((x + 1, y))
        elif b == "D":
            history.append((x, y - 1))
        elif b == "L":
            history.append((x - 1, y))
    elif a == "2":
        p = int(b)
        n = len(history)
        if p > n:
            print(f"{p-n} 0")
        else:
            k, j = history[n - p]
            print(f"{k} {j}")
