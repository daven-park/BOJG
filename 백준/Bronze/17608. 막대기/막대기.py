N = int(input())

stack = []
numbers = [int(input()) for num in range(N)]

stack.append(numbers[len(numbers) - 1])
for number in reversed(numbers):
    if number > stack[len(stack) - 1]:
        stack.append(number)


print(len(stack))