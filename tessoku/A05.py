import io
from operator import mod
import sys

_INPUT = """\
3000 4000


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n, k = map(int, input().split())
ans = 0

for n_i in range(1, n + 1):
    tmp = 0
    tmp = k - n_i

    if tmp <= 1:
        continue

    for j in range(1, n + 1):
        x = tmp
        x -= j

        if x <= 0 or x > n:
            continue
        ans += 1
print(ans)
