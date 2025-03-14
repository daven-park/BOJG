import sys

N = int(input())
decimalList = list(map(int, input().split()))

counter = [False] * 1001

for i in range(2, 1001):
    for j in range(i + i, 1001, i):
        counter[j] = True

cnt = 0
for num in decimalList:
    if num == 1: continue
    if not counter[num]:
        cnt += 1
print(cnt)

