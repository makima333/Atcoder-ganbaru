import io
from operator import mod
import sys

_INPUT = """\
10 500 999
38 420 490 585 613 614 760 926 945 999

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
n, h, x = map(int, input().split())
pp = list(map(int, input().split()))

for p_i, p in enumerate(pp):
    hp = h + p
    if hp >= x:
        print(p_i + 1)
        exit()
