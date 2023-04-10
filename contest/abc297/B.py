import io
from operator import mod
import sys

_INPUT = """\
BRKRBQNN



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

SS = list(input())

B_index = []
K_index = 0
R_index = []
for s_i, s in enumerate(SS):

    if s == "B":
        B_index.append(s_i)
    if s == "K":
        K_index = s_i
    if s == "R":
        R_index.append(s_i)


if (sum(B_index) % 2 == 1) and R_index[0] < K_index and R_index[1] > K_index:
    print("Yes")
else:
    print("No")
