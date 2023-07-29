import io
from operator import mod
import sys

_INPUT = """\
8
3 7 4 7 3 3 8 2

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------
n = int(input())

aa = list(map(int, input().split()))

graph =  [ 0 for _ in range(n+1)]

for a_i, a in enumerate(aa):
    graph[a_i+1] = a


for a_i, a in enumerate(aa):
    b1_idx = a_i+1
    history = [b1_idx, a]
    history_set = set(history)
    old_node = a
    
    while True:
        next_node = graph[old_node]
        graph[old_node] = 0
        if next_node in history_set or next_node == 0:
            if next_node in history_set:
                if aa[history[-1]-1] == history[0]:
                    print(len(history))
                    print(*history)
                    exit()
                else:
                    for h_i ,h in enumerate(  history):
                        if h == next_node:
                            tmp = history[h_i:]
                            print(len(tmp))
                            print(*tmp)
                            exit()
            break
        history.append(next_node)
        history_set.add(next_node)
        old_node = next_node

    