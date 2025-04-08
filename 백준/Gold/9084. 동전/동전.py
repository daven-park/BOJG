import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    coins = [num for num in map(int, input().split())]
    target = int(input())
    dp = [[0] * (target + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    # i번째 동전을 사용해서 j원을 만드는 방법의 수

    # 동전을 쓸지 안쓸지 판단하기
    for i in range(1, N + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i -1][j]

            # 현재 동전을 넣을 수 있을만큼 남아있다면
            if j - coins[i - 1] >= 0:
                dp[i][j] += dp[i][j - coins[i - 1]]
    print(dp[N][target])