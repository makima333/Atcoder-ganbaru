import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
1



"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())
yakusu = []

for j in range(1, 10, 1):
    if N % j == 0:
        yakusu.append((j, N // j))


# print(yakusu)
ans = []
for i in range(N + 1):
    if i == 0:
        ans.append("1")
        continue

    tmp = "-"
    for j, alpa in yakusu:
        if i % alpa == 0:
            tmp = str(j)
            break

    ans.append(tmp)

# print(ans)
print("".join(ans))
