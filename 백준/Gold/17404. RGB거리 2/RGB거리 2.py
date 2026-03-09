import sys

input = sys.stdin.readline
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
answer = float('Infinity')

for start in range(3):
    dp = [[float('Infinity')] * 3 for _ in range(N)]
    dp[0][start] = colors[0][start]
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + colors[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + colors[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + colors[i][2]

    for end in range(3):
        if end != start:
            answer = min(dp[N - 1][end], answer)
            
print(answer)