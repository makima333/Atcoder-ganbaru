import io
from operator import mod
import sys

_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
# 検索用：素因数分解
k = int(input())
ans = 0

for p in range(2, int(k ** (1 / 2)) + 1):
    a = 0
    while k % p == 0:
        k //= p
        a += 1

    n = 0
    while a > 0:
        n += p
        x = n
        while x % p == 0:
            x //= p
            a -= 1

    ans = max(ans, n)
ans = max(ans, k)
print(ans)
