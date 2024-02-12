n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse = True)
count = 0
for coin in coins:
    if k == 0:
        break
    count += (k // coin)
    # print(count)
    k = (k % coin)
print(count)