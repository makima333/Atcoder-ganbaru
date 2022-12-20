import io
from operator import mod
import sys

_INPUT = """\
3




"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("".join(list(alpha)[:n]))
