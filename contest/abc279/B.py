import io
from operator import mod
import sys

_INPUT = """\
toyotasystems
toyotasystems




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
s = input()
t = input()
if t in s:
    print("Yes")
else:
    print("No")
