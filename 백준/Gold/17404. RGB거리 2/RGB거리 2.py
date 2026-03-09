import sys

input = sys.stdin.readline

N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('Infinity')] * 3 for _ in range(N)]
answer = []
dp[0][0] = colors[0][0]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + colors[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + colors[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + colors[i][2]
answer.append(min(dp[N - 1][1], dp[N - 1][2]))

dp = [[float('Infinity')] * 3 for _ in range(N)]
dp[0][1] = colors[0][1]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1] , dp[i - 1][2]) + colors[i][0]
    dp[i][1] = min(dp[i - 1][0] , dp[i - 1][2]) + colors[i][1]
    dp[i][2] = min(dp[i - 1][0] , dp[i - 1][1]) + colors[i][2]
answer.append(min(dp[N - 1][0], dp[N - 1][2]))

dp = [[float('Infinity')] * 3 for _ in range(N)]
dp[0][2] = colors[0][2]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + colors[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + colors[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + colors[i][2]
answer.append(min(dp[N - 1][0], dp[N - 1][1]))

print(min(answer))