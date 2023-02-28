import io
from operator import mod
import sys

_INPUT = """\
aBc


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
ss = list(input())

big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i, s in enumerate(ss):
    if s in big:
        print(i + 1)
        exit()
