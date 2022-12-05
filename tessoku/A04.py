import io
from operator import mod
import sys

_INPUT = """\
13


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
print(format(int(input()), "010b"))
