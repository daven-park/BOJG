import sys

C = int(input())

for c in range(1, C + 1):
    scoreList = list(map(int, input().split()))
    N = scoreList.pop(0)
    total = 0
    avg = 0
    for i in scoreList:
        total += i
    avg = total // N
    cnt = 0
    for i in scoreList:
        if i > avg:
            cnt += 1
    ans = format((cnt / N) * 100, ".3f")
    print(ans + "%")
