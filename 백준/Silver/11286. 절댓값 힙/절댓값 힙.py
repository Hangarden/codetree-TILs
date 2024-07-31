import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    n = int(input())

    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            x = heapq.heappop((heap))
            print(x[1])
    else:
        heapq.heappush(heap, (abs(n), n))

