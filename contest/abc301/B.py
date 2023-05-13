import io
from operator import mod
import sys

_INPUT = """\
6
3 4 5 6 5 4


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
N = int(input())
aa = list(map(int, input().split()))
ans = []

def ab (a,b,c):
    # print( list(range(a,b,c)))
    return list(range(a,b,c))

for i in range(N):
    
    ans.append(aa[i])
    
    if i == N-1:
        pass
    
    elif aa[i]+1 == aa[i+1] or aa[i] == aa[i+1]+1:
        pass
    
    elif aa[i] > aa[i+1]:
        ans += list(range(aa[i]-1, aa[i+1], -1))
    
    elif aa[i] < aa[i+1]:
        ans += list(range(aa[i]+1, aa[i+1], 1))


print(*ans)        