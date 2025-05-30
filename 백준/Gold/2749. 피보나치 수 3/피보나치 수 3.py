import sys
input = sys.stdin.readline

N = int(input())

N = N % 1500000
dp = [0] * (N + 2)

dp[1] = 1
for i in range(2, N + 1):
    dp[i] = (dp[i - 2]  + dp[i - 1]) % 1000000

print(dp[N])