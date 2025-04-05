
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    weight, v = map(int, input().split())
    for max_weight in range(K + 1):
        if weight > max_weight:  # 현재 물건의 무게 > 현재 무게 한도
            dp[i][max_weight] = dp[i - 1][max_weight]     # 못담으면 이전 값 그대로
        else:                   # 이전 개수의 최대무게와 
            dp[i][max_weight] = max(dp[i - 1][max_weight], 
                                    dp[i - 1][max_weight - weight] + v)

print(dp[N][K])