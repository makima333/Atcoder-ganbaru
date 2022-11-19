import io
from operator import mod
import sys

_INPUT = """\
10
1 8 4 15 7 5 7 5 8 0
11
1 1
2 2 3
3 2
1 2
2 2 3
2 2 3
2 3 1
3 1
3 2
3 3
3 4

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import copy

n = int(input())
A = list(map(int, input().split()))
q_times = int(input())
init_array = [-1] * n
tmp_num = -1
calhis = {}


for _ in range(q_times):
    q = list(map(int, input().split()))
    # print(A)
    if q[0] == 1:
        A = init_array
        tmp_num = q[1]

    elif q[0] == 2:
        if tmp_num != -1:
            if A[q[1] - 1] == -1:
                A[q[1] - 1] = tmp_num + q[2]
                calhis[q[1] - 1] = [tmp_num, A[q[1] - 1]]
            else:
                if calhis[q[1] - 1][0] == tmp_num:
                    A[q[1] - 1] += q[2]
                    calhis[q[1] - 1] = [tmp_num, A[q[1] - 1]]
                else:
                    A[q[1] - 1] = tmp_num + q[2]
                    calhis[q[1] - 1] = [tmp_num, A[q[1] - 1]]

        else:
            A[q[1] - 1] += q[2]

    elif q[0] == 3:
        if tmp_num != -1:
            if A[q[1] - 1] == -1:
                print(tmp_num)
            else:
                if (q[1] - 1) in calhis.keys():
                    if calhis[q[1] - 1][0] == tmp_num:
                        print(A[q[1] - 1])
                    else:
                        print(tmp_num)
                else:
                    print(tmp_num)

        else:
            print(A[q[1] - 1])
