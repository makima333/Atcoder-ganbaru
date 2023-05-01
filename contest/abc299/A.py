import io
from operator import mod
import sys

_INPUT = """\
10
.|..*...|.


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
_ = input()
cc = list(input().replace(".", ""))

if cc[0] == "|" and cc[1] == "*":
    print("in")
else:
    print("out")
