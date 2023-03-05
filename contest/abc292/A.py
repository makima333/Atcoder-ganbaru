import io
from operator import mod
import sys

_INPUT = """\
abc



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
ss = input()

print(ss.upper())
