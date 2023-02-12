import io
from operator import mod
import sys

_INPUT = """\
4 2
2
1 2
2
1 3


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, m = map(int, input().split())
ac = []
all_ac = set({})

for _ in range(m):
    _ = input()
    tmp = list(map(int, input().split()))
    tmp_set = set(tmp)
    ac.append(tmp_set)

    all_ac = all_ac | tmp_set

if len(all_ac) != n:
    print(0)
    exit()

ans = 0
for i in range(2**m):
    comb = [int(j) for j in format(i, f"0{m}b")]
    # comb.sort(reverse=True)
    tmp_set = set([])
    # print(comb)
    for c_i, c in enumerate(comb):
        if c == 1:
            tmp_set = tmp_set | ac[c_i]

    if tmp_set == all_ac:
        ans += 1

print(ans)
