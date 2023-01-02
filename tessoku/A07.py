import io
from operator import mod
import sys

_INPUT = """\
8
5
2 3
3 6
5 7
3 7
1 5


"""
sys.stdin = io.StringIO(_INPUT)
# --------------------------------
D = int(input())
N = int(input())
B = [0] + [0] * (D + 1)


for idx in range(N):
    l, r = map(int, input().split())
    B[l] += 1
    B[r + 1] -= 1

ans: int = 0
for i in range(1, D + 1):
    ans += B[i]
    print(ans)
