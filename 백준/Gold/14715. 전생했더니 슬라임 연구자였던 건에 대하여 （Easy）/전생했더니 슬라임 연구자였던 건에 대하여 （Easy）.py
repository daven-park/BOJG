import math
import sys

input = sys.stdin.readline

K = int(input())

# 소수 판별 배열: False → 소수, True → 소수 아님
prime = [False] * 1000001
for i in range(2, 1001):
    if prime[i]:
        continue
    for j in range(i * i, 1000001, i):
        prime[j] = True

def recursive(N):
    if N < 2 or not prime[N]:  # 예외 처리 추가
        return 0
    answer = float('inf')
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            depth = 1 + max(recursive(i), recursive(N // i))
            answer = min(answer, depth)
    return answer

print(recursive(K))