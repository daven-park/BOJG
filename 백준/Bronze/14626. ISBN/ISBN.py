import sys

isbn = input().strip()

m = isbn[len(isbn) - 1]
sum = 0
is_even = False
for i in range(13):
    if isbn[i] != '*':
        sum += int(isbn[i]) if i % 2 == 0 else int(isbn[i]) * 3
    else:
        if i % 2 != 0:
            is_even = True
if is_even:
    for i in range(10):
        if (sum + (i * 3)) % 10 == 0:
            print(i)
            break
else:
    print(10 - sum % 10)