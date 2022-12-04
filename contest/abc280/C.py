import io
from operator import mod
import sys

_INPUT = """\
jfkdslajfkdlsalshkfjdlahsjklhaf
jfkdaslajfkdlsalshkfjdlahsjklhaf

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
s = set(map(lambda i: str(i[0] + 1).zfill(8) + i[1], enumerate(list(input()))))
t = set(map(lambda i: str(i[0] + 1).zfill(8) + i[1], enumerate(list(input()))))
tmp = t - s
tmp = list(tmp)
tmp.sort()
# print(tmp)
print(int(tmp[0][:-1]))
