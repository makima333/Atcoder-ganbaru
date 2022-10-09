import io
from operator import mod
import sys

_INPUT = """\
4
3 1
?01
4 2
?1?0
6 3
011?1?
10 5
01?1???00?

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

import sys
import copy

sys.setrecursionlimit(10**7)

t = int(input())
ans = []


def dfs(pre_s, tmp_k, lis, t_ans):
    if len(ans_list) > 2:
        return None

    if len(lis) == 0:
        return t_ans

    while True:
        if len(lis) == 0:
            if len(t_ans) == n and tmp_k == 0:
                ans_list.append(t_ans)
            break

        s = lis.pop(0)
        if s == "1":
            if tmp_k == 0:
                # 詰み
                return t_ans
            tmp_k -= 1
            t_ans += s
            pre_s = "1"

        if s == "0":
            t_ans += s
            pre_s = "0"

        if s == "?":
            if tmp_k == 0:
                t_ans += "0"
                pre_s = "0"
            elif pre_s == "1":
                tmp_k -= 1
                t_ans += "1"
                pre_s = "1"
            else:
                pre_s = "0"
                tmp_copy = copy.copy(lis)
                tmp = dfs(pre_s, tmp_k, tmp_copy, t_ans + "0")
                if tmp is not None and len(tmp) == n and tmp_k == 0:
                    ans_list.append(tmp)

                pre_s = "1"
                tmp_copy = copy.copy(lis)
                tmp = dfs(pre_s, tmp_k - 1, tmp_copy, t_ans + "1")
                if tmp is not None and len(tmp) == n and tmp_k == 0:
                    ans_list.append(tmp)


for _ in range(t):
    n, k = map(int, input().split())
    s_list = list(input())
    tmp_ans = ""
    pre_s = ""
    ans_list = []
    dfs(pre_s, k, s_list, tmp_ans)
    if len(ans_list) == 1:
        print("Yes")
    else:
        print("No")
