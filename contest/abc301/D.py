import io
from operator import mod
import sys

_INPUT = """\
??0?
0



"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
ss  = input()

N = int(input())
Nbin = format(N, "b")

if len(Nbin) <= len(ss):
    hatena = []
    for i, s in enumerate(list(ss)) :
        if s == "?":
            hatena.append(i)
    
    hatena = sorted(hatena, reverse=False)
    ss = "".join(ss).replace("?","0")
    
    if  N < int(ss,2):
        print(-1)
        exit()
    
    ss = list(ss)
    for hate in hatena:
        ss[hate] = "1"
        # print(ss)
        tmp = "".join(ss)
        if  N < int(tmp,2):
            ss[hate] = "0"
    
    print(int("".join(ss),2))
else:
    print(int(ss.replace("?","1"),2))
    

