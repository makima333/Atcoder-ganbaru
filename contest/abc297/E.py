import io
from operator import mod
import sys

_INPUT = """\
4 2
1 10 1 100

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n, k = map(int, input().split())

aa = list(map(int, input().split()))

aa.sort()
aa = set(aa)

import heapq


def heap(N, K, prices):
    min_heap = []
    his = set([])
    for price in prices:
        his.add(price)
        heapq.heappush(min_heap, price)

    count = 0
    while count < K:
        current_min = heapq.heappop(min_heap)
        count += 1

        for price in prices:
            if current_min + price not in his:
                his.add(current_min + price)
                heapq.heappush(min_heap, current_min + price)

    return current_min


print(heap(n, k, aa))
