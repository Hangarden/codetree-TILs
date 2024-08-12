fibo = [0 for _ in range(50)]
fibo[0] = 1
fibo[1] = 1
for i in range(2,48):
    fibo[i] =fibo[i-1] + fibo[i-2]

n = int(input())

print(fibo[n-1])