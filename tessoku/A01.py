import io
from operator import mod
import sys

_INPUT = """\
10



"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
print(int(input()) ** 2)
