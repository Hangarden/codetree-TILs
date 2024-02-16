n = int(input())

count = 0
while n > 1:
    if n == 0:
        break

    if n >= 5:
        count += (n // 5)
        n %= 5
    else:
        count += (n//2)
        n %= 2


if n== 0:
    print(count)
else:
    print(-1)