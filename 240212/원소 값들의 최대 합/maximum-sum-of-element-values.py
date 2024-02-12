n, m = map(int, input().split())

lst = list(map(int, input().split()))
array = []
for i, x in enumerate(lst):
    array.append((i,x))

# print(array)
max_val = -1
for i in range(n):
    count = 0
    sums = 0
    while count < m:
        value = array[i][1]
        # print(value)
        sums += value
        i = value -1
        count +=1
    max_val = max(max_val, sums)

print(max_val)