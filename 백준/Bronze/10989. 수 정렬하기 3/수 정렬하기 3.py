import sys

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
N = int(input())

numbers = [0] * 10001

for i in range(N):
    num = int(input())
    numbers[num] += 1


for idx, cnt in enumerate(numbers):
    if cnt != 0:
        for i in range(cnt):
            print(idx)
    else:
        continue
