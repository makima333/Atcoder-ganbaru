import io
from operator import mod
import sys

_INPUT = """\
8 6
0 1 2 1 2 2 2 5

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

import collections


n, m = map(int, input().split())
a_lis = list(map(int, input().split()))
a_lis.sort()
total = sum(a_lis)
a_set = list(set(a_lis))
nums_sum = collections.Counter(a_lis)
# sum_max = 0

tmp_sum = 0
i = 0
ans = []
while i != len(a_set):
    curr_num = a_set[i]
    tmp_sum += nums_sum[curr_num] * curr_num

    if i == len(a_set) - 1 or curr_num + 1 != a_set[i + 1]:
        # print(tmp_sum)
        ans.append(tmp_sum)
        tmp_sum = 0

    i += 1

if len(ans) > 1:
    if a_set[0] == 0 and a_set[-1] + 1 == m:
        ans[0] += ans[-1]

print(total - max(ans))
