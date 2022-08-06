import io
import sys

_INPUT = """\
3
1 2

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n = int(input())
p = [0, 0]+list(map(int, input().split()))

cnt = 0
while n != 1:
    cnt += 1
    n = p[n]
print(cnt)