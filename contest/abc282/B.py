import io
from operator import mod
import sys

_INPUT = """\
2 4
xxxx
oxox


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())

ss = []
for _ in range(n):
    row = input()
    tmp = set([])
    for c_i, c in enumerate(list(row)):
        if c == "o":
            tmp.add(c_i + 1)

    ss.append(tmp)

import copy

cnt = 0
# ss_i = 0
while len(ss) != 1:
    tmp_s = ss.pop(0)
    # print(tmp_s, ss)

    for s in ss:
        if len(s | tmp_s) == m:
            # print(s | tmp_s)
            cnt += 1
    # ss_i += 1
print(cnt)
