import io
from operator import mod
import sys

_INPUT = """\
31 9 24 31 24




"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n_lis = list(input().split())

dict = {}
for n in n_lis:
    dict[n] = 0

print(len(dict))
