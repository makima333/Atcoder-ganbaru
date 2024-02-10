import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

rec_dict = {}


def dfs(x):
    tmp = x
    if x in rec_dict:
        return rec_dict[x]

    if x == 2:
        return 2
    elif x == 1:
        return 0

    if x % 2 == 0:
        tmp += dfs(x // 2) * 2
    else:
        tmp += dfs((x // 2) + 1)
        tmp += dfs(x // 2)

    rec_dict[x] = tmp
    return tmp


print(int(dfs(N)))
# print(rec_dict)
