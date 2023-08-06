import io
from operator import mod
import sys

_INPUT = """\
10
999999997 999999999 4 3 2 4 999999990 8 999999991 999999993

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
aa = list(map(int, input().split()))

aa.sort()
suma = sum(aa)

bb = [suma // n for _ in range(n)]

for i in range(suma % n):
    bb[i] += 1

bb.sort()
ans = sum([abs(aa[i] - bb[i]) for i in range(n)])

print(ans // 2)
