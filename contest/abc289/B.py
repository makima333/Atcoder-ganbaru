import io
from operator import mod
import sys

_INPUT = """\
10 6
1 2 3 7 8 9




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())
aa = list(map(int, input().split()))
aa_set = set(aa)

if m == 0:
    for i in range(n):
        print(i + 1, end=" ")
    exit()

a_g = []

for i in range(1, n + 1):
    if i == 1:
        a_g.append([1])
        continue

    if i - 1 in aa_set:
        a_g[-1].append(i)
    else:
        a_g.append([i])


for a_lis in a_g:
    a_lis.sort(reverse=True)
    for a in a_lis:
        print(a, end=" ")
