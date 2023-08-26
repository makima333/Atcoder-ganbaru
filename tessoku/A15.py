import io
from operator import mod
import sys

_INPUT = """\
5
11 12 12 11 11

"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
N = int(input())
AA = list(map(int, input().split()))
aa_set = set(AA)
from collections import defaultdict

conv_map = defaultdict(int)

for a_i, a in enumerate(sorted(list(aa_set))):
    conv_map[a] = a_i + 1

for a in AA:
    print(conv_map[a], end=" ")
