import sys

T = int(input())

for t in range(1, T + 1):
    oxString = input()
    arr = [char for char in oxString]

    prev = 0
    ans = 0
    for i in arr:
        if i == 'O':
            prev += 1
            ans += prev

        elif i == 'X':
            prev = 0
    print(ans)
