import io
from operator import mod
import sys

_INPUT = """\
9 7
3 0 2 5 5 3 0 6 3


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

import collections


n, m = map(int, input().split())
a_lis = list(map(int, input().split()))
total = sum(a_lis)
a_set = set(a_lis)

nums_sum = {}
for i in a_set:
    nums_sum[i] = i * a_lis.count(i)

print(collections.Counter(a_lis).items()[1])


histroy = set([])
ans = []
while len(a_set):
    # for i in a_set:
    sum = 0
    i = list(a_set)[0]

    curent_i = i
    while True:
        histroy.add(curent_i)
        sum += nums_sum[curent_i]
        if (curent_i + 1) % m in a_set:
            curent_i = (curent_i + 1) % m
        else:
            break

    a_set = a_set - histroy
    ans.append(sum)


print(total - max(ans))
