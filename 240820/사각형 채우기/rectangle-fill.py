dp = [0 for _ in range(1001)]

dp[1], dp[2] = 1, 2

n = int(input())

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
# print(dp)
print(dp[n] % 10007)