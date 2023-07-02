import io
from operator import mod
import sys

_INPUT = """\
0 23 24 145 301 413 631 632




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
ss = list(map(int, input().split()))


res = False

for s_i, s in enumerate(ss):
    if s_i != 0:
        if s < ss[s_i - 1]:
            print("No")
            exit()

    if s < 100 or s > 675:
        print("No")
        exit()

    if s % 25 != 0:
        print("No")
        exit()


print("Yes")
