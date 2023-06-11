import io
from operator import mod
import sys

_INPUT = """\
7 50
11 12 16 22 27 28 31


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, k = map(int, input().split())
aa = list(map(int, input().split()))

R = [0 for _ in range(n)]
ruiseki = [0]
for a in aa:
    ruiseki.append(ruiseki[-1] + a)


for a_i, a in enumerate(aa):

    if a_i != 0:
        R[a_i] = R[a_i - 1]
    elif a_i == 0:
        R[0] = -1

    while R[a_i] < n - 1:
        tmp_sum = ruiseki[R[a_i] + 2] - ruiseki[a_i]
        if tmp_sum <= k:
            R[a_i] += 1
        else:
            break

ans = 0
# 連続する番号は１つのみ選択する場合も含むので、＋１
for i, r in enumerate(R):
    ans += r - i + 1
print(ans)
