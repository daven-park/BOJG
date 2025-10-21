import sys

N = int(input())

weights = [int(input()) for _ in range(N)]

weights.sort(reverse=True)

max_weight = 0
for i in range(N):
    weight = weights[i] * (i + 1)
    max_weight = max(max_weight, weight)

print(max_weight)