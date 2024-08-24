import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
1 1 100

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
A = list(map(int, input().split()))
ans = 0

while True:
    cnt = [0] * 100
    # check
    for a in A:
        if a > 0:
            cnt[a - 1] += 1

    if sum(cnt) <= 1:
        break

    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1

    ans += 1

print(ans)
