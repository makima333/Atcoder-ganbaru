import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
30
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
_ = input()

dd = list(map(int, input().split()))

ans = 0
for m, d in enumerate(dd):
    month = m + 1
    for day in range(1, d + 1):
        md = str(day) + str(month)
        if len(set(list(md))) == 1:
            ans += 1


print(ans)
