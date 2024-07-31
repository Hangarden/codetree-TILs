import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    x = int(input())
    if x != 0:
        q.append(x)
    else:
        q.pop()
    # print(q)


print(sum(q))