from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = -2
    # 1. 각 큐의 합을 구합니다
    total = sum(q1) + sum(q2)
    
    # 2-0. 홀수일때는?
    if total % 2 != 0:
        return -1
    # 2. 두 큐의 합을 맞추기 위해 현재 두 큐의 차 // 2가 될 수 있는 원소들의 합을 구합니다
    half = total // 2

    # 2-1. 가능한 원소를 찾는 탐색?
    # --> 길이 최대 300000, 완전탐색으로 O(n2)으로 불가능
    # --> 투포인터로 가능한 값 찾기? O(n)으로 가능할지도?
    # --> 값이 정렬되어있지 않아서 투포인터 불가능
    # --> 슬라이딩 윈도우로 하프가 가능한 값이 존재하는지 체크?
    # half값의 원소가 존재하면 해당 
    
#     def search(a, b, target):
#         flag = False
#         left = 0
#         right = 
    # 2-2 큐의 원소를 뺴서 자신의 원소에 삽입 불가?
    # -> 순차적으로 원소가 같이 있지 않는한 불가능한가?
    # 두큐의 차 // 2가 되는 원소가 존재한다면 해당 원소를 제외하고 
    # 3. 해당 원소들을 옮길 수 있을때까지 큐를 돌립니다?
    
    # 빠지고 넣어야할 값들을 지속적으로 계산할 수 있다면??
    firstSum = sum(q1)
    secondSum = sum(q2)
    cnt = 0
    while firstSum != secondSum:
        # 만약 둘중 한 큐에 원소가 모두 사라졌다면 break
        if firstSum == 0 or secondSum == 0: return -1
        if cnt > (len(q1) + len(q2)) * 2:
            return -1
        if firstSum > secondSum:
            temp = q1.popleft()
            q2.append(temp)
            firstSum -= temp
            secondSum += temp
        elif firstSum < secondSum:
            temp = q2.popleft()
            q1.append(temp)
            firstSum += temp
            secondSum -= temp
        cnt += 1
        
    return cnt