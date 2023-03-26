import io
from operator import mod
import sys

_INPUT = """\
20230322





"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
from collections import Counter

ss = list(input())
nums_cnt = [0] * 10
bit_cnts = []
bit_cnts.append("".join(map(str, nums_cnt)))

for s in ss:
    nums_cnt[int(s)] ^= 1 << int(s)
    bit_cnts.append("".join(map(str, nums_cnt)))

ans = 0
for k, v in Counter(bit_cnts).items():

    ans += v * (v - 1) // 2

print(ans)
