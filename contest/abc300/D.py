import io
from operator import mod
import sys

_INPUT = """\
1000


"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
N = int(input())
Z = int(1e6)


isprime = [True for _ in range(Z + 1)]
cnt_prime = [0 for _ in range(Z + 1)]
primes = []

isprime[0] = False
isprime[1] = False

for p in range(2, int(Z ** (1 / 2)) + 1):
    if isprime[p]:
        for q in range(p * p, Z + 1, p):
            isprime[q] = False

for p in range(2, Z + 1):
    if isprime[p]:
        primes.append(p)
        cnt_prime[p] = 1

for p in range(2, Z + 1):
    cnt_prime[p] += cnt_prime[p - 1]


ans = 0
for i in range(len(primes)):
    a = primes[i]
    if a >= N ** (1 / 5):
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a * a * b * b * b >= N:
            break
        ans += cnt_prime[int((N // (a * a * b)) ** (1 / 2))] - cnt_prime[b]


print(ans)
