import io
from operator import mod
import sys

_INPUT = """\
3 3
oox
oxo
xoo


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, d = map(int, input().split())

ss = [list(input()) for _ in range(n)]

dd_cnt = 0
dd_max = 0

for d in range(d):
    dd_flg = True
    for s in ss:
        if s[d] != "o":
            dd_flg = False
        
        if dd_flg == False:
            dd_max = max(dd_cnt, dd_max)
            dd_cnt = 0
            break
    else:
        dd_cnt += 1
        dd_max = max(dd_cnt, dd_max)

print(dd_max)
    