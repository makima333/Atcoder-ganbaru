import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5
0 3 2 8 12


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (2 * 10**5 + 1)
ans = 0

for a in A:
    x, i = a, 2
    while i * i <= x:
        while x % (i * i) == 0:
            x //= i * i
        i += 1
    ans += cnt[x]
    cnt[x] += 1


print(ans + cnt[0] * (N - cnt[0]))
