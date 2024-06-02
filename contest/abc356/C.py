import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
11 4 9
10 1 2 3 4 5 6 7 8 9 10 o
11 1 2 3 4 5 6 7 8 9 10 11 o
10 11 10 9 8 7 6 5 4 3 2 x
10 11 9 1 4 3 7 5 6 2 10 x


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N, M, K = map(int, input().split())
C = []
R = []
A = []
for _ in range(M):
    line = input().split()
    C.append(int(line[0]))
    A.append(list(map(int, line[1:-1])))
    R.append(line[-1])

ans = 0


def check(keys):
    for a_i, a in enumerate(A):
        total = 0
        for a_ in a:
            total += keys[a_ - 1]

        if R[a_i] == "o":
            if total < K:
                return False
        else:
            if total >= K:
                return False
    return True


ans = []
from copy import copy


def dfs(i, keys):
    if i == N:
        if check(keys):
            ans.append(1)
        return

    new_keys = keys.copy()
    dfs(i + 1, new_keys + [1])
    new_keys = keys.copy()
    dfs(i + 1, new_keys + [0])


dfs(1, [1])
dfs(1, [0])

print(len(ans))

# bit search, bit全探索
ans = 0
# 1 << N は 2^N
for bit in range(1 << N):
    # bit変換
    keys = [(bit >> i) & 1 for i in range(N)]
    if check(keys):
        ans += 1
print(ans)
