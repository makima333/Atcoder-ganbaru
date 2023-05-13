import io
from operator import mod
import sys

_INPUT = """\
1
A



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
ss = input()

acnt = 0
tcnt = 0

if n % 2 == 0:
    limit = n // 2
else:
    limit = (n // 2) +1

for s in ss:
    if s == "T":
        tcnt += 1
        if tcnt  == limit:
            print("T")
            exit()
    else:
        acnt += 1
        if acnt == limit:
            print("A")
            exit()

    