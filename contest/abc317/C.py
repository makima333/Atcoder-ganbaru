import io
from operator import mod
import sys

_INPUT = """\
4 4
1 2 1
2 3 10
1 3 100
1 4 1000


"""
sys.stdin = io.StringIO(_INPUT)
# ---------------------------------
import sys

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
geo = [[] for _ in range(N + 1)]
city_type = set([])


for _ in range(M):
    a, b, c = map(int, input().split())
    geo[a].append((b, c))
    geo[b].append((a, c))
    city_type.add(a)
    city_type.add(b)


anss = []
city_type_num = len(city_type)


def dfs(city, history, total_length):
    # print(city, total_length)
    history.add(city)

    if len(history) > 1:
        anss.append(total_length)

    for dist, length in geo[city]:
        if dist not in history:
            dfs(dist, history.copy(), total_length + length)


for i in range(1, N + 1):
    dfs(i, set([i]), 0)

print(max(anss))
