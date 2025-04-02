import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
numbers = [0] + [int(input()) for num in range(N)]
total = sum(numbers)
dp = [0] * (N + 1)
if N <= 2:
    print(total)
    sys.exit()
dp[1] = numbers[1]
dp[2] = numbers[2]
dp[3] = numbers[3]

for k in range(4, N):
    dp[k] = min(dp[k - 2], dp[k - 3]) + numbers[k]

print(total - min(dp[N - 1], dp[N - 2]))