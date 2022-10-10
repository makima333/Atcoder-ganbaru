import io
from operator import mod
import sys

_INPUT = """\
4
3 2
1??
4 2
?1?0
6 3
011?1?
10 5
00?1???10?

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
t = int(input())
ans = []


for _ in range(t):
    n, k = map(int, input().split())

    sum_1 = [0]
    sum_0 = [0]

    for s in input():
        sum_1.append(sum_1[-1] + (s == "1"))
        sum_0.append(sum_0[-1] + (s == "0"))

    cnt = 0
    for j in range(n - k + 1):
        if sum_1[j] == 0 and sum_1[n] == sum_1[j + k] and sum_0[j + k] == sum_0[j]:
            cnt += 1

    print("Yes" if cnt == 1 else "No")
