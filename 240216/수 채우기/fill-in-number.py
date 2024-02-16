n = int(input())

D = [999999999999] * (100001)
D[0] = 0

for i in range(2, n+1):
    if i < 5:
        D[i] = min(D[i], D[i-2]) +  1
    else:
        D[i] = min(D[i], D[i-2], D[i-5]) + 1
# print(D)

if D[n] >= 999999999999:
    print(-1)
else:
    print(D[n])