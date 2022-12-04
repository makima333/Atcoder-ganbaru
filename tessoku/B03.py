import io
from operator import mod
import sys

_INPUT = """\
10
50 150 250 350 450 550 650 750 850 950



"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
import copy

n = input()
nums_1 = list(map(int, input().split()))


for i, n_1 in enumerate(nums_1):
    nums_2 = copy.copy(nums_1)
    nums_3 = copy.copy(nums_1)
    nums_2.pop(i)
    nums_3.pop(i)
    for j, n_2 in enumerate(nums_2):
        for n_3 in nums_3:
            if n_2 != n_3 and n_1 + n_2 + n_3 == 1000:

                print("Yes")
                exit()
print("No")
