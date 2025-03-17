import sys

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
N = int(input())

numbers = []

for i in range(N):
    number = int(input())
    numbers.append(number)


numbers = list(set(numbers))
numbers.sort()

for i in numbers:
    print(i)