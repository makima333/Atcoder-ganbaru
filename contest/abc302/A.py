import io
from operator import mod
import sys

_INPUT = """\
999999999999999998 2



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
a, b = map(int, input().split())

cnt = 0
from decimal import Decimal

if Decimal(a) % Decimal(b) == 0:
    print(Decimal(a) // Decimal(b))
else:
    print(Decimal(a) // Decimal(b) + 1)
