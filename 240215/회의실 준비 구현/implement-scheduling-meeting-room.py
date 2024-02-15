n = int(input())

minutes = [tuple(map(int, input().split())) for _ in range(n)]

minutes.sort(key = lambda x : x[1])

# print(minutes)

curr_end = 0
count = 0
for start, end in minutes:
    if start >= curr_end:
        curr_end = end 
        count += 1

print(count)