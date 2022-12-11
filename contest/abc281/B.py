import io
from operator import mod
import sys

_INPUT = """\
Q142857Z



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = list(input())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if len(n) != 8:
    print("No")
    exit()

if n[0] not in alpha:
    print("No")
    exit()

if n[-1] not in alpha:
    print("No")
    exit()

try:
    tmp = int("".join(n[1 : len(n) - 1]))
    if tmp < 100000:
        raise
    print("Yes")
except:
    print("No")
    exit()
