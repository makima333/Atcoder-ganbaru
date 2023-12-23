import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
-2 2 2 8



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
A, M, L, R = map(int, input().split())


def logic(lr):
    global M
    global A

    return abs(A - lr) // M


if M == 1:
    ans = (R - L) + 1
elif A < L:
    ans = logic(R) - logic(L - 1)

elif A > R:
    ans = logic(L) - logic(R + 1)
else:
    ans = logic(L) + logic(R) + 1

print(ans)
