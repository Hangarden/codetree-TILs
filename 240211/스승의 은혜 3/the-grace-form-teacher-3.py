# 8 22
import heapq
N, B = map(int, input().split())
present = []
for _ in range(N):
    # a, b = map(int, input().split())
    # heapq.heappush(present, (a+b, (a, b)))
    present.append(list(map(int, input().split())))
present.sort(key = lambda x : (x[0] + x[1]))

# print(present)
max_val = -1
def find(present):
    global max_val
    sums = 0
    count = 0
    while sums <= B and count < N:
        sums += sum(present[count])
        count += 1
    max_val = max(max_val, count)
    return
    
for i in range(N):
    x = present[i][0]
    present[i][0] = (x//2)
    find(present)
    present[i][0] = (x*2)

print(max_val)
# total = 0 
# for i in present:

#     if total > B: