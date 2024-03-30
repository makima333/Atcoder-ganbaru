import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
123456789012345



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

import math

N = int(input())
num = 1


# 回文
# retrun : boolean
def kaibun(c):
    return c == c[::-1]


max_num = 1
while True:
    num3 = int(math.pow(num, 3))
    # print(num3)
    if num3 > N:
        break

    if kaibun(str(num3)):
        max_num = num3
    num += 1
print(max_num)
