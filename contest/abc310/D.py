import io
from operator import mod
import sys

_INPUT = """\
6 4 0


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
from copy import copy
# 再帰, チーム分け
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

n, t, m = map(int, input().split())
from itertools import combinations

teams = []
unmatch = [set() for _ in range(n+1)]
people = list(range(1,n+1))

ans = 0

for _ in range(m):
    a,b = map(int, input().split())
    unmatch[a].add(b)
    unmatch[b].add(a)


def create_team(people, teams):
    global ans
    # 最後の人
    if people == n+1:
        # team に最低一人ずついる
        if len(teams) == t:
            ans +=1
        return
    
    # 相性が悪くなければ、各チームに追加
    for team in teams:
        for peaple_t in team:
            if peaple_t in unmatch[people]:
                break
        else:
            team.append(people)
            create_team(people+1, copy(teams))
            team.pop()
    
    if (len(teams) < t):
        teams.append([people])
        create_team(people+1, copy(teams))
        # teams.pop()

create_team(1, [])
print(ans)