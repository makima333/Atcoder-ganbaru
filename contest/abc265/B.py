import io
import sys

_INPUT = """\
4 0 10
10 7 5
2 10



"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n, m, t= map(int, input().split())
a_arr =[0] + list(map(int, input().split())) 

bonus_dict = {}
for _ in range(m):
    k, v= map(int, input().split())
    bonus_dict[k] = v

for i  in range(1,n):
    if i in bonus_dict.keys():
        t += bonus_dict[i]

    t -= a_arr[i]
    
    if t <= 0:
        print('No')
        exit()

print('Yes')