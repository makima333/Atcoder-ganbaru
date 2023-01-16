import io
from operator import mod
import sys

_INPUT = """\
6
abcbac


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
t = int(input())

s = list(input())

for moji_i, moji in enumerate(s):
    if moji_i == 0:
        continue
    cnt = 0
    tmp = moji_i
    j = 0
    while j + moji_i < len(s):
        if s[j] != s[j + moji_i]:
            cnt += 1
        else:
            break
        j += 1
    print(cnt)
