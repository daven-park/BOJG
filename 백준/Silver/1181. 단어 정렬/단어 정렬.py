import sys

N = int(input())

words = []

for i in range(N):
    word = input()
    words.append(word)
# set으로 중복제거한 값을 다시 list로 변환
words = list(set(words))
# 길이로 검사 후 사전순 내림차순 정렬
words.sort(key=lambda a : (len(a), a))

for word in words:
    print(word)