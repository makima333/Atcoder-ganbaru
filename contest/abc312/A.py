import io
from operator import mod
import sys

_INPUT = """\
FAC


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
s = input()
ss = set(["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"])

if s in ss:
    print("Yes")
else:
    print("No")
