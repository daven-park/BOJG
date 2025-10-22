import sys
from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())

    answer = 1
    clothes = defaultdict(int)
    for i in range(N):
        name, kind = map(str, input().split())
        clothes[kind] += 1

    for cnt in clothes:
        answer *= clothes[cnt] + 1

    print(answer - 1)