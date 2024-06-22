import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10 50000
120190 165111 196897 456895 540000 552614 561627 743796 757613 991216

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, A = map(int, input().split())
T = list(map(int, input().split()))

current_time = T[0]
ans = []
while True:
    t = T.pop(0)
    if current_time == t:
        ans.append(t + A)
        current_time = t + A
    elif current_time < t:
        ans.append(t + A)
        current_time = t + A
    else:
        ans.append(current_time + A)
        current_time = current_time + A
    if len(T) == 0:
        break

[print(a) for a in ans]
