n = int(input())

D = [-1] * (n+2)
D[2],D[4], D[5] = 1, 2, 1


for i in range(6, n+1):
    if D[i-2] != -1 or D[i-5] != -1:
        if D[i-2] == -1:
            D[i] = D[i-5] + 1
        elif D[i-5] == -1:
            D[i] = D[i-2] + 1
    continue
# print(D)
print(D[n])