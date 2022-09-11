import io
from multiprocessing import current_process
import sys

_INPUT = """\
4
3 2 0 1


"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n = int(input())
n_lis = list(map(int, input().split()))

cnts = [ 0 for _ in range(n)]
for i, food in enumerate(n_lis):
    dir = food - 1
    cnts[dir - i] += 1
    dir = food 
    cnts[dir - i] += 1
    dir = food + 1 if food + 1 <= n-1 else 0
    cnts[dir - i] += 1

print(max(cnts))   