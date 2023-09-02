import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
8 3 1000000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, D, P = map(int, input().split())
ff = list(map(int, input().split()))

# チケット枚数を導出
ff.sort(reverse=True)

ff_sums = [0]
for f in ff:
    if len(ff_sums) == 0:
        ff_sums.append(f)
    else:
        ff_sums.append(ff_sums[-1] + f)

current_day = 0
freepass = 0
while True:
    a = ff_sums[current_day]
    if current_day + D <= N - 1:
        b = ff_sums[current_day + D]
    else:
        b = ff_sums[-1]

    c = b - a
    if c < P:
        break

    freepass += 1
    if b == ff_sums[-1]:
        break
    current_day = current_day + D

if current_day <= N - 1 and D * freepass < N:
    print((freepass * P) + ff_sums[-1] - ff_sums[current_day])
else:
    print(freepass * P)
