import io
from operator import mod
import sys

_INPUT = """\
8 3
apzbqrcs
1 2 3 1 2 2 1 2



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N, M = map(int, input().split())

S = list(input())
C = list(map(int, input().split()))

str_list = ["" for _ in range(M + 1)]
for i in range(N):
    str_list[C[i]] = str_list[C[i]] + S[i]

for i in range(1, M + 1):
    tmp = str_list[i]
    str_list[i] = tmp[-1] + tmp[:-1]

ans = ""
for i in C:
    tmp = str_list[i]
    ans += tmp[0]
    str_list[i] = tmp[1:]

print(ans)
