import io
from operator import mod
import sys

_INPUT = """\
21
0 20 62 192 284 310 323 324 352 374 409 452 486 512 523 594 677 814 838 946 1000
10
77 721
255 541
478 970
369 466
343 541
42 165
16 618
222 592
730 983
999 1000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
aa = list(map(int, input().split()))

q_n = int(input())


sleeps = []

# 累積睡眠時間
for i in range(n):
    if i == 0:
        sleeps.append(0)

    elif i % 2 == 1:
        sleeps.append(sleeps[i - 1])

    elif i % 2 == 0:
        sleeps.append(sleeps[i - 1] + (aa[i] - aa[i - 1]))


import bisect

for _ in range(q_n):
    l, r = map(int, input().split())

    bl = bisect.bisect_left(aa, l)
    # print(bl)
    if bl % 2 == 0:
        sleep_l = aa[bl] - l
        bl += 1
    else:
        sleep_l = 0

    br = bisect.bisect_left(aa, r)
    # print(",", br)
    if br % 2 == 0:
        sleep_r = aa[br] - r
    else:
        sleep_r = 0
        br -= 1

    try:
        sleep_time = (sleeps[br] - sleeps[bl]) + sleep_l - sleep_r
    except:
        sleep_time = (sleeps[br] - sleeps[bl - 1]) + sleep_l - sleep_r

    print(sleep_time)
