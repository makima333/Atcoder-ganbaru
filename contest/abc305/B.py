import io
from operator import mod
import sys

_INPUT = """\
C F

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(str, input().split())

ndict = {
    "A": 0,
    "B": 3,
    "C": 4,
    "D": 8,
    "E": 9,
    "F": 14,
    "G": 23,
}


print(abs(ndict[n] - ndict[m]))
