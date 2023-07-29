import io
from operator import mod
import sys

_INPUT = """\
21 25
#########################
#..............###...####
#..............#..#...###
#........###...#...#...##
#........#..#..#........#
#...##...#..#..#...#....#
#..#..#..###...#..#.....#
#..#..#..#..#..###......#
#..####..#..#...........#
#..#..#..###............#
#..#..#.................#
#........##.............#
#.......#..#............#
#..........#....#.......#
#........###...##....#..#
#..........#..#.#...##..#
#.......#..#....#..#.#..#
##.......##.....#....#..#
###.............#....#..#
####.................#..#
#########################

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
from copy import copy

from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

h,w = map(int, input().split())

grid = [list(input()) for _ in range(h)]

player = (1,1)
history= set([player])
ans = 1

def move(act):
    global player
    global ans
    new_player = player
    if act == "r":
        while grid[new_player[0]][new_player[1]] == ".":
            player = new_player
            if player not in history:
                ans += 1
                history.add(player)
            new_player = (player[0], player[1]+1)
    if act == "l":
        while grid[new_player[0]][new_player[1]] == ".":
            player = new_player
            if player not in history:
                ans += 1
                history.add(player)
            new_player = (player[0], player[1]-1)
    if act == "u":
        while grid[new_player[0]][new_player[1]] == ".":
            player = new_player
            if player not in history:
                ans += 1
                history.add(player)
            new_player = (player[0]-1, player[1])
    if act == "d":
        while grid[new_player[0]][new_player[1]] == ".":
            player = new_player
            if player not in history:
                ans += 1
                history.add(player)
            new_player = (player[0]+1, player[1])
    

from collections import deque
tasks = deque()
tasks.append((player,"r"))
tasks.append((player,"l"))
tasks.append((player,"u"))
tasks.append((player,"d"))
move_history = set([player])

while len(tasks) > 0:
    player, action = tasks.popleft()
    # print(player, action)
    move(action)
    if player not in move_history:
        move_history.add(player)    
        tasks.append((player,"r"))
        tasks.append((player,"l"))
        tasks.append((player,"u"))
        tasks.append((player,"d"))


print(ans)
    
    