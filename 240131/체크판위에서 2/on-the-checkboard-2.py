def find(target, i, j):
    count = 0
    for x in range(i+1, r-1):
        for y in range(j+1, c-1):
            if array[x][y] != target:
                count += 1
    # print(count)
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
else:
    if array[0][0] == array[r-1][c-1]:
        print(0)
    else:
        print(sums)