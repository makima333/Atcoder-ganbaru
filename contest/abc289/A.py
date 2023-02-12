import io
from operator import mod
import sys

_INPUT = """\
01

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
s = input()
s = s.replace("0", "2")
s = s.replace("1", "0")
s = s.replace("2", "1")

print(s)
