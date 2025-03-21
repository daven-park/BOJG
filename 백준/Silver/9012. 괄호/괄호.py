import sys

N = int(input())

input = sys.stdin.readline
result = []

def check_parenthesis(parenthesis, stack):
    for parent in parenthesis:
        if parent == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True if len(stack) == 0 else False

for t in range(N):
    stack = []
    parenthesis = [char for char in input().strip()]
    if check_parenthesis(parenthesis, stack):
        print("YES")
    else:
        print("NO")