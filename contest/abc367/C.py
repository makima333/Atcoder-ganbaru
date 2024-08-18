import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1 2
1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, K = map(int, input().split())
R = list(map(int, input().split()))
ans = []


def check(arr):
    sum_arr = sum(arr)
    if sum_arr % K == 0:
        ans.append(arr)
    return


def dfs(idx, tmp_ans):
    if len(tmp_ans) == N:
        check(tmp_ans)
        return

    max_r = R[idx]

    for i in range(1, max_r + 1):
        dfs(idx + 1, tmp_ans + [i])


dfs(0, [])
if len(ans) > 0:
    for a in ans:
        print(*a)
