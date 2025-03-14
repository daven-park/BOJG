string = input().strip()

words = list(map(str, string.split(" ")))
if not string:
    print(0)
else:
    print(len(words))