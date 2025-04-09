import sys

input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + sorted(list(set(A[1:])), reverse=True)

dp = [[0] * (N + 1) for _ in range(len(B))]

for i in range(1, len(B)):
    for j in range(1, N + 1):
        if A[j] == B[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j - 1])

print(dp[len(B) - 1][N])