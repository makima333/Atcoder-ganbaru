import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
3 1 2

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

ans = []


def solve(A):
    N = len(A)
    for i in range(N):
        while A[i] != i + 1:
            swap_idx = A[i] - 1
            A[i], A[swap_idx] = A[swap_idx], A[i]
            ans.append((i + 1, swap_idx + 1))

    return A


# 入力例
N = int(input())
A = list(map(int, input().split()))


result = solve(A)
print(len(ans))
for a in ans:
    print(*a)
