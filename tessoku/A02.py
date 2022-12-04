import io
from operator import mod
import sys

_INPUT = """\
5 70
10 20 30 40 50



"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
n, x = map(int, input().split())
As = list(map(int, input().split()))

print("Yes" if x in As else "No")
