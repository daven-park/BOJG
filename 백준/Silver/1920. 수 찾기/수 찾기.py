import sys

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
targets = list(map(int, input().split()))

def binary_search(targetnumber):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == targetnumber:
            return 1
        elif numbers[mid] < targetnumber:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for target in targets:
    print(binary_search(target))