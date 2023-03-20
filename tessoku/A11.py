import io
from operator import mod
import sys

_INPUT = """\
10 80
10 20 30 40 50 60 70 80 90 100


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
# 2分探索
import bisect

n, x = map(int, input().split())
aa = list(map(int, input().split()))

print(bisect.bisect(aa, x))
