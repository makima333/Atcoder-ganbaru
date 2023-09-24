import io
from operator import mod
import sys

# 再帰用
sys.setrecursionlimit(10**9)


_INPUT = """\
777


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------

import copy
import sys

# 再帰用
sys.setrecursionlimit(10**9)
ans = []


def dfs(tmp, nums, keta):
    if len(tmp) == keta:
        ans.append(int("".join(tmp)))
        return 0

    for n_i, n in enumerate(nums):
        if tmp == []:
            tmp_list = copy.copy(tmp)
            tmp_list.append(str(n))
            if n_i == len(nums) - 1:
                dfs(tmp_list, [], keta)
            else:
                dfs(tmp_list, nums[n_i + 1 :], keta)
        else:
            if int(tmp[-1]) > int(n):
                tmp_list = copy.copy(tmp)
                tmp_list.append(str(n))
                if n_i == len(nums) - 1:
                    dfs(tmp_list, [], keta)
                else:
                    dfs(tmp_list, nums[n_i + 1 :], keta)


nums = list(range(10))
nums.sort(reverse=True)
for i in range(1, 11):
    dfs([], nums, i)

ans.sort()
print(ans[int(input())])
# print(ans)
