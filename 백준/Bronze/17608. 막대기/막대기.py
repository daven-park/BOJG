N = int(input())

stack = []
numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

stack.append(numbers[len(numbers) - 1])
for number in reversed(numbers):
    if number > stack[len(stack) - 1]:
        stack.append(number)

print(len(stack))