import io
from operator import mod
import sys

_INPUT = """\
5


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())


dbg = [0] * n
# cnt = 0
for i in range(1, n):
    cnt = 0
    for j in range(1, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            tmp = i / j

            if j == tmp:
                cnt += 1
            else:
                cnt += 2
    dbg[i] = cnt

# print(dbg)
ans = 0
for i in range(1, int(n / 2) + 1):
    # print(i, n - i)
    tmp = 2
    if i == n - i:
        tmp = 1
    ans += dbg[i] * dbg[n - i] * tmp


print(ans)
