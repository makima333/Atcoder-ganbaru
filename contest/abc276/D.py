import io
from operator import mod
import sys

_INPUT = """\
3
1 4 3


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import math

n = int(input())
a_l = list(map(int, input().split()))
g = a_l[0]
cnt = 0


for a in a_l:
    g = math.gcd(g, a)

for a in a_l:
    a /= g
    while a % 2 == 0:
        a //= 2
        cnt += 1

    while a % 3 == 0:
        a //= 3
        cnt += 1

    if a != 1:
        print(-1)
        exit()

print(cnt)
