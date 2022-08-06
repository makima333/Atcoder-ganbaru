import io
import sys

_INPUT = """\
1 10
"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
def dfs(A):
    if len(A) == n:
        print(*A)
        return 0
    init = 1
    

    for i in range(m):
        tmp = [init+i] 
        if len(A) == 0 or A[-1] < init+i:
            dfs(A+tmp)


n, m = map(int, input().split())
dfs([])