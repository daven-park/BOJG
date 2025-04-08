import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 2)
for i in range(1, N + 1):
    time, price = map(int, input().split())
    if i + time <= N + 1:
        dp[i + time] = max(dp[i + time], dp[i] + price)
    dp[i + 1] = max(dp[i + 1], dp[i])
print(max(dp))