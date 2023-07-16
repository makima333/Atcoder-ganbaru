import io
from operator import mod
import sys

_INPUT = """\
20 10
72036 3 3 4 9
7716 4 1 2 3 6
54093 5 1 6 7 8 10
25517 7 3 4 5 6 7 9 10
96930 8 2 3 4 6 7 8 9 10
47774 6 2 4 5 6 7 9
36959 5 1 3 4 5 8
46622 7 1 2 3 5 6 8 10
34315 9 1 3 4 5 6 7 8 9 10
54129 7 1 3 4 6 7 8 9
4274 5 2 4 7 9 10
16578 5 2 3 6 7 9
61809 4 1 2 4 5
1659 5 3 5 6 9 10
59183 5 1 2 3 4 9
22186 4 3 5 6 8
98282 4 1 4 7 10
72865 8 1 2 3 4 6 8 9 10
33796 6 1 3 5 7 9 10
74670 4 1 2 6 8


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n,m = map(int, input().split())
prods = []

# 0 p
# 1 c
# 2 set(function)
for _ in range(n):
    tmp = []
    in_list = list(map(int, input().split()))
    tmp.append(in_list[0])
    tmp.append(in_list[1])
    tmp.append(set(in_list[2:]))

    prods.append(tmp)


for i, prod_i in enumerate( prods):
    for j, prod_j in enumerate(prods):
        if i == j:
            continue
        if prod_i[0] >= prod_j[0]:
        # J が上位集合 or もしくは同一
            if prod_i[2].issubset(prod_j[2]):
                if prod_i[0] > prod_j[0] or prod_j[1] > prod_i[1]:
                    print("Yes")
                    exit()
print("No")        