import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
10000000000



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
MOD = 998244353
N = int(input())
p10 = pow(10, len(str(N)), MOD)

print(N * (1 - pow(p10, N, MOD)) * pow(1 - p10, -1, MOD) % MOD)
