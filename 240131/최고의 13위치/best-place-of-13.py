n = int(input())
max_val = 0
array =[]
for _ in range(n):
    array.append(list(map(int, input().split())))

for j in range(n):
    for i in range(n-2):
        max_val = max(max_val, array[j][i] + array[j][i+1] + array[j][i+2])

print(max_val)