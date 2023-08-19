import io
from operator import mod
import sys

_INPUT = """\
1
1

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------


M = int(input())
DD = list(map(int, input().split()))


DD_sum = [DD[0]]
for i in range(1, M):
    DD_sum.append(DD_sum[-1] + DD[i])


import bisect

year_total = sum(DD) + 1
search_result = bisect.bisect_left(DD_sum, year_total / 2) + 1

if search_result > 1:
    day = (year_total // 2) - DD_sum[search_result - 2]
else:
    day = year_total // 2

print(search_result, day)
