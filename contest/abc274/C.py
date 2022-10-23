import io
from operator import mod
import sys

_INPUT = """\
4
1 3 5 2

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ns = map(int, input().split())

# key = num , value = gen
ndict = {}
gen = 0
for i, num in enumerate(ns):
    tmp_i = i + 1
    if num not in ndict.keys():
        ndict[num] = 0
    ndict[2 * tmp_i] = ndict[num] + 1
    ndict[2 * tmp_i + 1] = ndict[num] + 1

for j in range(2 * n + 1):
    tmp_j = j + 1
    print(ndict[tmp_j])
