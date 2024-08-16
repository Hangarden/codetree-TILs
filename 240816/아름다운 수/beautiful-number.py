from itertools import product
beautiful = ['1', '22', '333', '4444']
count = 0

n = int(input())
for i in product(beautiful, repeat=n):
    x = "".join(i)
    if len(x) > n:
        continue
    else:
        count += 1
print(count)