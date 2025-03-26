import sys

input = sys.stdin.readline

stack = []
ans = 0
brackets = [char for char in input()]
temp = 1
valid = True
for i in range(len(brackets)):
    b = brackets[i]

    if b == '(':
        temp *= 2
        stack.append(b)
    elif b == '[':
        temp *= 3
        stack.append(b)
    elif b == ')':
        if not stack or stack[-1] != '(':
            valid = False
            break
        if brackets[i - 1] == '(':
            ans += temp
        stack.pop()
        temp //= 2
    elif b == ']':
        if not stack or stack[-1] != '[':
            valid = False
            break
        if brackets[i - 1] == '[':
            ans += temp
        stack.pop()
        temp //= 3

if not valid or stack:
    print(0)
else:
    print(ans)