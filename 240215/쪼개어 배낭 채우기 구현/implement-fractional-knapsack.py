n, m  = map(int, input().split())
# list(map(int, input().split())) for _ in range(n)
jewelyes = []

for _ in range(n):
    weight, value = map(int, input().split())
    jewelyes.append(((value/weight), weight, value))

jewelyes.sort(reverse = True)
# print(jewelyes)

value = 0

for i in jewelyes:
    if m <= 0:
        break

    if m - i[1] > 0:
        value += i[2]
        m -= i[1]
    elif m - i[1] <= 0:
        value += m * i[0]
        m = 0

print(format(round(value,3), '.3f'))