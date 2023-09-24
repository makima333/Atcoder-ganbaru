import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
86411


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = input()
if len(list(N)) == 1:
    print("Yes")
    exit()

tmp = [99]
for n in list(N):
    if tmp[-1] <= int(n):
        print("No")
        exit()
    tmp.append(int(n))

print("Yes")
