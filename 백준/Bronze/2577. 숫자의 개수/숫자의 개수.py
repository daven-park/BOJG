import sys

total = 1
for _ in range(3):
    num = int(input())
    total *= num

countArray = [0 for i in range(10)]

strList = f"{total}"

for num in strList:
    countArray[int(num)] += 1

for num in countArray:
    print(num)
