import io
import sys

_INPUT = """\
5
1 100 1000 10000 123

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n = int(input())

a_lis =list(map(int, input().split())) 
a_lis.sort(reverse=True)
tmp = list(map(str,a_lis[:3]))
tmp = sorted(tmp, reverse=True)
print("".join(tmp))
