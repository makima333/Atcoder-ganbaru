"""Module providingFunction printing python version."""
import io
import sys
from operator import mod

_INPUT = """\



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, k  = map(int, input().split())
import numpy as np

aa = np.array(input().split(),dtype=int)
bb = np.array(input().split(),dtype=int)
cc = np.array(input().split(),dtype=int)
dd = np.array(input().split(),dtype=int)

pp = (aa[:, np.newaxis] + bb).flatten()
qq = set((cc[:, np.newaxis] + dd).flatten())

for p in pp:
    if k - p in qq:
        print("Yes")
        exit()

print('No')
