n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

max_val = 0
if n ==1:
    max_val = array[0][0]
else:
    for i in range(1,n):
        array[0][i] = array[0][i-1] + array[0][i]
    for i in range(1,n):
        array[i][0] = array[i-1][0] + array[i][0]

    for i in range(1, n):
        for j in range(1, n):
            array[i][j] = max(array[i-1][j] + array[i][j], array[i][j-1] + array[i][j])
    for i in range(n):
        max_val = max(max(array[i]), max_val)

print(max_val)