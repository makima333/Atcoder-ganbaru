import io
from operator import mod
import sys

_INPUT = """\
5
1 3 3 3 1
2
4
3


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
# 2分探索
import bisect

n = int(input())
aa = list(map(int, input().split()))
aa.sort()
q = int(input())

for _ in range(q):
    x = int(input())
    print(bisect.bisect_left(aa, x))
