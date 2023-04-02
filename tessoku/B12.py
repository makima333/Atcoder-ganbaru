import io
from operator import mod
import sys

_INPUT = """\
30


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------

from decimal import Decimal

n = int(input())

left = Decimal(1)
right = Decimal(100000)


def logic(mid):
    return mid**3 + mid


while round(left, 3) < round(right, 3):
    mid = (left + right) / Decimal(2)
    cal_res = logic(mid)
    # print(left, right)
    if cal_res < n:
        left = mid + Decimal(0.0001)
    else:
        right = mid


print(round(left, 3))
