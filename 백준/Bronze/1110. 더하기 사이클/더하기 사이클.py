import sys

N = int(input())

cnt = 1

def getSum(number):
    total = 0
    while number != 0:
        total += number % 10
        number //= 10
    return total

compare = int(str(N % 10)  + str(getSum(N) % 10))
while N != compare:
    compare = int(str(compare % 10) + str(getSum(compare) % 10))
    cnt += 1

print(cnt)