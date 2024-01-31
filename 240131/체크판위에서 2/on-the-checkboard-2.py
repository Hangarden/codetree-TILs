def find(target, i, j):
    count = 0
    for i in range(i+1, r-1):
        for j in range(j+1, c-1):
            if array[i][j] != target:
                count += 1
    return count

r, c = map(int, input().split())

array = []

for _ in range(r):
    array.append(list(input().split()))


S = []
S.append(array[0][0])

start = array[0][0]

sums = 0
for i in range(1, r-1):
    for j in range(1, c-1):
        if array[i][j] != start:
            sums += find(array[i][j], i, j)

print(sums)