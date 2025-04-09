import sys

input = sys.stdin.readline

N = int(input())
dp = [[0] * N for _ in range(N)]

p = [tuple(map(int, input().split())) for _ in range(N)]

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = float("inf")
        for k in range(i, j):
             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + (p[i][0] * p[k][1]  * p[j][1]))

print(dp[0][N - 1])