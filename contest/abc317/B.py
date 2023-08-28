import io
from operator import mod
import sys

_INPUT = """\
16
152 153 154 147 148 149 158 159 160 155 156 157 144 145 146 150

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
aa = list(map(int, input().split()))


aa.sort()
for a_i, a in enumerate(aa):
    if a_i == 0:
        continue

    if aa[a_i - 1] + 1 != a:
        print(a - 1)
        exit()
