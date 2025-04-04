import sys
import re

input = sys.stdin.readline

N = int(input())

if N <= 2:
    print(N)
    sys.exit()
    
dp = [0] * (N + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[N] % 15746)