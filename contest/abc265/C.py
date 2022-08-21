import io
from multiprocessing import current_process
import sys

_INPUT = """\
9 44
RRDDDDRRRDDDRRRRRRDDDRDDDDRDDRDDDDDDRRDRRRRR
RRRDLRDRDLLLLRDRRLLLDDRDLLLRDDDLLLDRRLLLLLDD
DRDLRLDRDLRDRLDRLRDDLDDLRDRLDRLDDRLRRLRRRDRR
DDLRRDLDDLDDRLDDLDRDDRDDDDRLRRLRDDRRRLDRDRDD
RDLRRDLRDLLLLRRDLRDRRDRRRDLRDDLLLLDDDLLLLRDR
RDLLLLLRDLRDRLDDLDDRDRRDRLDRRRLDDDLDDDRDDLDR
RDLRRDLDDLRDRLRDLDDDLDDRLDRDRDLDRDLDDLRRDLRR
RDLDRRLDRLLLLDRDRLLLRDDLLLLLRDRLLLRRRRLLLDDR
RRRRDRDDRRRDDRDDDRRRDRDRDRDRRRRRRDDDRDDDDRRR

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------

h, w =map(int, input().split())
grid =  [list(map(str, list(input()))) for _ in range(h)]


curr_x = 0
curr_y = 0
history = set("x_1,y_1")
while curr_x >= 0 and curr_x < h and curr_y >= 0 and curr_y < w:
    move_str = grid[curr_x][curr_y]
    tmp_x = curr_x
    tmp_y = curr_y

    if move_str ==  'U':
        curr_x -= 1
    elif move_str == 'D':
        curr_x += 1
    elif move_str == 'L':
        curr_y -= 1
    elif move_str == 'R':
        curr_y += 1
    
    next_xy = f"x_{curr_x+1},y_{curr_y+1}"
    if next_xy in history:
        print(-1)
        exit()
    else:
        history.add(next_xy)


if len(history) > 1:
    print(tmp_x+1, tmp_y+1)
else:
    print("1 1")
