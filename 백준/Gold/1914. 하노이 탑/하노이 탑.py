import sys

N = int(input())

def hanoi(num, start, rest, dest):
    if num == 1:
        print(start, dest)
        return
    else:
        hanoi(num - 1, start, dest, rest)   # n번째를 dest로 옮기기 위해서는 n - 1번째를 rest로 옮겨놔야 한다
        hanoi(1, start, rest, dest)
        hanoi(num - 1, rest, start, dest)

print(2**N - 1)
if N <= 20 :
    hanoi(N, 1, 2, 3)