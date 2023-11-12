import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
5 1
aaaaa
1 5


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, Q = map(int, input().split())

S = list(input())

cnt = [0 for _ in range(N)]
cnt_tmp = 0
for s_i, s in enumerate(S):
    if s_i == 0:
        continue

    if s == S[s_i - 1]:
        cnt_tmp += 1
    cnt[s_i] = cnt_tmp

for _ in range(Q):
    left, right = map(int, input().split())
    print(cnt[right - 1] - cnt[left - 1])
