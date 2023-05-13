import io
from operator import mod
import sys

_INPUT = """\
atcoder
@@@@@@@



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------

import string

alphabet_dict_s = {letter: 0 for letter in string.ascii_lowercase}
alphabet_dict_s["@"] = 0
alphabet_dict_t = {letter: 0 for letter in string.ascii_lowercase}
alphabet_dict_t["@"] = 0


ss = list(input())
tt = list(input())

for s in ss:
    alphabet_dict_s[s] += 1

for t in tt:
    alphabet_dict_t[t] += 1

atcoder = set([ "a", 't', 'c', 'o', 'd', "e", 'r'])

at_cnt_s = alphabet_dict_s["@"]
at_cnt_t = alphabet_dict_t["@"]

for key in alphabet_dict_s:
    if key == "@":
        pass
    elif alphabet_dict_s[key] != alphabet_dict_t[key]:
        if key not in  atcoder:
            print("No")
            exit()
        else:
            if alphabet_dict_s[key] > alphabet_dict_t[key]:
                at_cnt_t -= (alphabet_dict_s[key] - alphabet_dict_t[key])
            else:
                at_cnt_s -= (alphabet_dict_t[key] - alphabet_dict_s[key])
    if at_cnt_s < 0 or at_cnt_t < 0:
        print("No")
        exit()

print("Yes")