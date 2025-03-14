import sys

a, b = map(int, input().split())
sanggen = [char for char in str(a)][::-1]
sangsu = [char for char in str(b)][::-1]

for i in range(3):
    if sanggen[i] > sangsu[i]:
        print(int("".join(sanggen)))
        break
    elif sanggen[i] < sangsu[i]:
        print(int("".join(sangsu)))
        break
    else:
        continue
