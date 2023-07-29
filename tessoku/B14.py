import io
from operator import mod
import sys

_INPUT = """\
6 30
5 1 18 7 2 9

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
n, k = map(int, input().split())
aa = list(map(int, input().split()))

from itertools import combinations


def all_comb_sum(array):
    sum_list = [0]
    for n in range(1, len(array) + 1):
        for comb in combinations(array, n):
            sum_list.append(sum(comb))
    return sum_list


bb = aa[: n // 2]
cc = aa[n // 2 :]

b_sum = set(all_comb_sum(bb))
c_sum = set(all_comb_sum(cc))

for bs in b_sum:
    target = k - bs
    if target in c_sum:
        print("Yes")
        exit()

print("No")
