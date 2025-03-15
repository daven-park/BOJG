import sys

# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

N = int(input())

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(N))