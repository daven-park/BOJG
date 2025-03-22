N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = len(numbers) - 1
min_total = float('inf')
ans = []
while left < right:
    total = numbers[left] + numbers[right]
    if abs(min_total) > abs(total):
        min_total = total
        ans = [numbers[left], numbers[right]]
    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        break

print(*sorted(ans))