import io
from operator import mod
import sys

_INPUT = """\
5
00
AA
XX
YY
ZZ

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

his = []

for _ in range(n):
    t_str = input()
    t = list(t_str)
    ans = True

    if t[0] not in "HDCS":
        ans = False

    if t[1] not in "A23456789TJQK":
        ans = False

    if t_str in his:
        ans = False

    if ans == False:
        print("No")
        exit()

    his.append(t_str)

print("Yes")
