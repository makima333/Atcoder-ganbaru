import io
from operator import mod
import sys

_INPUT = """\
7 10
11 12 16 22 27 28 31


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, k = map(int, input().split())
aa = list(map(int, input().split()))

# しゃくとり法
R = [0 for _ in range(n)]

for a_i, a in enumerate(aa):
    if a_i != 0:
        R[a_i] = R[a_i - 1]

    # if R[a_i] == a_i:
    #     R[a_i] += 1

    tmp_diff = 0
    while R[a_i] + 1 != n:
        tmp_diff = aa[R[a_i] + 1] - a
        if tmp_diff <= k:
            R[a_i] += 1
        else:
            break

ans = 0
for i, r in enumerate(R):
    ans += r - i

print(ans)
