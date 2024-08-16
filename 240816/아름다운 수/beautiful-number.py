from itertools import product
beautiful = ['1', '22', '333', '4444']
count = 0

n = int(input())

for k in range(n+1):
    for i in product(beautiful, repeat=k):
        # print(i)
        x = "".join(i)
        # print(x)
        if len(x) == n:
            count += 1
print(count)