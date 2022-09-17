import io
from multiprocessing import current_process
import sys

_INPUT = """\
11

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
import copy


n = int(input())
nbin = list(str(bin(n))[2:])
base = ["0" for _ in range(len(nbin))]
res = [0]
one_index_list = []
for i, b in enumerate(nbin):
    if b == "1":
        one_index_list.append(i)


c_oil = copy.copy(one_index_list)
while len(c_oil) != 0:
    cal = copy.copy(base)
    tmp = c_oil.pop(0)
    cal[tmp] = "1"
    if len(c_oil) == 0:
        res.append(int("".join(cal), 2))
        break
    current = 0
    for i in range(2 ** len(c_oil)):
        cal_res = copy.copy(cal)

        bits = list(format(i, f"0{len(c_oil)}b"))
        # print(bits)
        for bit_i, bit in enumerate(bits):
            if bit == "1":
                cal_res[c_oil[bit_i]] = "1"
        # print("".join(cal_res))
        res.append(int("".join(cal_res), 2))
    # break

res.sort()
for r in res:
    print(r)
