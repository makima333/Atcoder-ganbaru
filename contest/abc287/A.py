import io
from operator import mod
import sys

_INPUT = """\
3 3
142857
004159
071028
159
287
857

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
for_cnt = 0
for _ in range(n):
    tmp = input()
    if tmp == "For":
        for_cnt += 1
    else:
        for_cnt -= 1


if for_cnt > 0:
    print("Yes")
else:
    print("No")
