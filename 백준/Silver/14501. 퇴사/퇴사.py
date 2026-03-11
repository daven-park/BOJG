import sys

input = sys.stdin.readline

N = int(input())

T = [0]
P = [0]
dp = [0] * (N + 2)
# 최대 이익 구하기
for i in range(N):
    t1, p1 = map(int, input().split())
    T.append(t1)
    P.append(p1)

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])

    if i + T[i] <= N + 1:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

    dp[i + 1] = max(dp[i + 1], dp[i])


print(dp[N + 1])