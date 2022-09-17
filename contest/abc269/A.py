import io
from operator import mod
import sys

_INPUT = """\
10 -20 30 -40

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
a,b,c,d = map(int, input().split())

print((a+b)*(c-d))
print('Takahashi')