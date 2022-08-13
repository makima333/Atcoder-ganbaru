import io
import sys

_INPUT = """\
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
2 3
6 8 9
16 18 19

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------

a_r, a_c =map(int, input().split())
a_matrix =  [list(map(int, input().split())) for _ in range(a_r)]
b_r, b_c =map(int, input().split())
b_matrix =  [list(map(int, input().split())) for _ in range(b_r)]
a_matrix_t = [list(x) for x in zip(*a_matrix)]
b_matrix_t = [list(x) for x in zip(*b_matrix)]


res = True
def check(a_matrix, b_matrix, res):
    for b_row in b_matrix:
        b_set = set(b_row)
        while True:
            if len(a_matrix) == 0:
                res = False
                break
            a_row = a_matrix.pop(0)
            a_set = set(a_row)
            if b_set <= a_set:
                a_diff = a_set ^ b_set
                a_tmp = [a for a in a_row if a not in a_diff]
                if len(a_set) == 1 and len(b_set) == 1 and a_set == b_set:
                    break
                if b_row == a_tmp:
                    break
            else:
                continue

        if res == False: break
    return res

res_1 = check(a_matrix, b_matrix, res)
res_2 = check(a_matrix_t, b_matrix_t, res)
if res_1 and res_2:
    print("Yes")
else:
    print("No")