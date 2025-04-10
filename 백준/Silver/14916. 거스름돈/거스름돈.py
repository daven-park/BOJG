import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(-1)
    sys.exit()

dp = [100001] * (N + 1)
dp[0] = 0
for i in range(N + 1):
    if i - 2 >= 0:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if i - 5 >= 0:
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[N] == 100001:
    print(-1)
else:
    print(dp[N])