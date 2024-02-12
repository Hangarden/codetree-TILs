# test = [[0,1],[0,99],[0,50]]

# test.sort(key = lambda x : x[1])

# print(test)

n = int(input())
tables = [(0,0)]
for _ in range(n):
    tables.append(tuple(map(int, input().split())))

tables.sort(key = lambda x : x[1])
# print(tables)

now = 0
count = 0
for start, end in tables:
    if start < now:
        count += 1
        continue
    now = end

print(count)