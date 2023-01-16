import io
from operator import mod

_INPUT = """\
5
a b
b a
z y
c d
y z

"""
import sys

sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

l_history = set([])
r_history = set([])

lr_dict = {}
rl_dict = {}

for _ in range(n):
    l, r = input().split()
    l_history.add(l)
    r_history.add(r)
    lr_dict[l] = r
    rl_dict[r] = l

# if l_history == r_history:
#     print("No")
#     exit()

import copy

ans_lr = copy.copy(lr_dict)
# ans_rl = copy.copy(rl_dict)
change_enable_list = []


for l, r in lr_dict.items():
    if r not in l_history:
        ans_lr.pop(l)
        # ans_rl.pop(r)
        if l in r_history:
            change_enable_list.append(l)

for r in change_enable_list:
    tmp_r = r
    while True:
        l = rl_dict[tmp_r]
        ans_lr.pop(l)
        if l in rl_dict.keys():
            tmp_r = l
        else:
            break

if len(ans_lr) > 1 and set(ans_lr.keys()) == set(ans_lr.values()):
    print("No")
else:
    print("Yes")
