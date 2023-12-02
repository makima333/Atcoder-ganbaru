import io
from operator import mod
import sys

# 再帰用
# sys.setrecursionlimit(10**9)


_INPUT = """\
50
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

N = int(input())

AA = list(map(int, input().split()))

AA_sorted = sorted(AA)
ruiseki = [0]

for a in AA_sorted:
    ruiseki.append(ruiseki[-1] + a)

ruiseki = ruiseki[1:]
from bisect import bisect_right

ans_his = {}

ans = []

for a in AA_sorted:
    if a in ans_his.keys():
        ans.append(ans_his[a])
        continue

    right_idx = bisect_right(AA_sorted, a)
    if right_idx < len(AA_sorted):
        # print(f"a={a}, {ruiseki[right_idx - 1]}")
        tmp = ruiseki[-1] - ruiseki[right_idx - 1]

    else:
        tmp = 0

    ans.append(tmp)
    ans_his[a] = tmp


re_ans = []

for a in AA:
    re_ans.append(ans_his[a])
# print(ans_his)
print(*re_ans)
