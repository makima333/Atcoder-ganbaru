import io
from multiprocessing import current_process
import sys

_INPUT = """\
10 4
-3 1 -4 1 -5 9 -2 6 -5 3

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n, m = map(int, input().split())

n_lis = list(map(int, input().split()))

sums = []
csums = [n_lis[0]]
for i in range(1,len(n_lis)):
    csums.append(csums[i-1] + n_lis[i])

for i in range(len(n_lis)):
    tmp_sum = 0
    if i == 0:
        for sum_i, n in enumerate( n_lis[i:i+m]) :
            tmp_sum += (sum_i+1)*n
    else:
        sum_old =  sums[i-1]
        if i == 1:
            current_sum = csums[m-1]
            tmp = 0
        else:
            current_sum = csums[i+m-2]
            tmp =  csums[i-2]

        sum_old -= (current_sum - tmp)
        tmp_sum = sum_old + (n_lis[i+m-1]*m)
          

    sums.append(tmp_sum)
    if i+m == len(n_lis):
        break

print(max(sums))