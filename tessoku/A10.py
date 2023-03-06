import io
from operator import mod
import sys

_INPUT = """\
7
1 2 5 5 2 3 1
2
3 5
4 6


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n = int(input())

aa = list(map(int, input().split()))
d = int(input())

l_to_r_max = []
max_tmp = 0
for a in aa:
    max_tmp = max(max_tmp, a)
    l_to_r_max.append(max_tmp)

r_to_l_max = []
max_tmp = 0
for i in range(n - 1, -1, -1):
    max_tmp = max(max_tmp, aa[i])
    r_to_l_max.append(max_tmp)


l_to_r_max = [0] + l_to_r_max + [0]
r_to_l_max = [0] + r_to_l_max + [0]

for _ in range(d):
    l, r = map(int, input().split())

    print(max(l_to_r_max[l - 1], r_to_l_max[len(aa) - r]))
