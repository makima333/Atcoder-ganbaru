import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10 5
abcwxyzyxw


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, K = map(int, input().split())
S = input()


def check_kaibun(s):
    left = 0
    right = K

    while right < len(s) + 1:
        tmps = s[left:right]
        # print(tmps)
        if tmps == tmps[::-1]:
            return True
        left += 1
        right += 1

    return False


import itertools


def generate(s):
    perms = itertools.permutations(s)
    return set(["".join(p) for p in perms])


if len(S) == len(set(S)):
    import math

    print(math.factorial(N))
    exit()

tmp = generate(S)

cnt = 0
for t in tmp:
    if check_kaibun(t) is False:
        cnt += 1
        # print(t)
    # else:
# print(len(tmp))
print(cnt)
