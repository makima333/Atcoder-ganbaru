import io
from multiprocessing import current_process
import sys

_INPUT = """\
6 1 2
3 1
2 5
1 2
4 1
2 6


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import sys

sys.setrecursionlimit(10**7)

n, x, y = map(int, input().split())
# points = [list(map(int, input().split())) for _ in range(n - 1)]

leaf = {i + 1: [] for i in range(n)}
seen = [0] * (n + 1)

for _ in range(n - 1):
    p = list(map(int, input().split()))
    leaf[p[0]].append(p[1])
    leaf[p[1]].append(p[0])


def dfs(in_num, ans):
    # if y in ans:
    #     return ans
    if in_num == y:
        print(*ans)
        exit()

    for l in leaf[in_num]:
        if seen[l]:
            continue
        seen[l] = 1
        ans.append(l)
        dfs(l, ans)
        ans.pop()


seen[x] = 1
dfs(x, [x])
