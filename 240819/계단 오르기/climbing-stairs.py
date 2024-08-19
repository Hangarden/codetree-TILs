# n개의 계단 2,3계단 위로만 올라갈 수 있다
# 1계단만 남은 경우는 올라갈 방법이 없음


# 2 -> 1
# 3 -> 1
# 4 -> 1
# 5 =? 2 3 3 2
n = int(input())
dp = [0 for _ in range(n+2)]

dp[0], dp[1]  = 1,0

for i in range(n+1):
    if n >= 3:
        dp[n] = dp[n-2] + dp[n-3]
    else:
        dp[n] = dp[n-2]
print(dp[n] % 10007)