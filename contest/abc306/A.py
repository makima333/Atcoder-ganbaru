import io
from operator import mod
import sys

_INPUT = """\
8
beginner


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
_ = int(input())

ss = list(input())


for s in ss:
    print(f"{s}{s}", end="")

# print("")
