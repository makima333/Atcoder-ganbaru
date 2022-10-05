import io
from operator import mod
import sys

_INPUT = """\
28


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a = int(input())

a = str(hex(a))[2:]


a = a.upper()
if len(list(a)) == 1:
    print(f"0{a}")
else:
    print(a)
