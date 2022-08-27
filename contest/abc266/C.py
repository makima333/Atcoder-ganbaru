import io
from multiprocessing import current_process
import sys

_INPUT = """\
0 0
1 1
-1 0
1 -1

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
import numpy as np
from numpy import linalg as LA
import math


def tangent_angle(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return  np.cross(u, v)

def call_tangent_angle(k, t, n) -> np.ndarray:
    kt = t - k
    kn = n - k
    return tangent_angle(kt, kn)


ax, ay =map(int, input().split())
bx, by =map(int, input().split())
cx, cy =map(int, input().split())
dx, dy =map(int, input().split())

a = np.array([ax, ay])
b = np.array([bx, by])
c = np.array([cx, cy])
d = np.array([dx, dy])

tmp = []
tmp.append(call_tangent_angle(a, b, d))
tmp.append(call_tangent_angle(b, c, a))
tmp.append(call_tangent_angle(c, d, b))
tmp.append(call_tangent_angle(d, a, c))

if min(tmp)>0:
    print("Yes")
else:
    print("No")