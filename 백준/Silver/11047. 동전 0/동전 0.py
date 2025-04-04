import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 가장 큰 순서부터 차례대로 카운팅
coins = [int(input()) for _ in range(N)]

cnt = 0
while K > 0 :
    for i in range(len(coins) - 1, -1, -1):
        if K // coins[i] >= 1:
            cnt += K // coins[i]
            K %= coins[i]
            break
print(cnt)