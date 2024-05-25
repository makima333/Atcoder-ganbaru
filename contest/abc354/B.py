import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
3
takahashi 2813
takahashixx 1086
takahashix 4229


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
sum_score = 0
names = []
for _ in range(N):
    name, score = input().split()
    sum_score += int(score)
    names.append(name)

names.sort(reverse=False)
print(names[sum_score % N])
