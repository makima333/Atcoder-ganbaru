import io
import sys
from tokenize import Double

_INPUT = """\
-9982443530000

"""
sys.stdin = io.StringIO(_INPUT)

#---------------------------------
n = int(input())

if n % 998244353 == 0:
    x = 0
elif n >= 0 and n <= 998244353:
    x = (-1)* (998244353 - n)
elif n > 998244353:
    tmp = n // 998244353
    tmp = 998244353 * tmp
    x = (n - tmp)
elif n < 0 and n >= -998244353:
    x = (998244353 - abs(n))
elif n < -998244353:
    tmp = abs(n) // 998244353
    tmp = 998244353 * (tmp+1)
    x =  tmp + n


print(x)

#---------------------------------

print(f'kensan n= {n}', (n-x)%998244353)