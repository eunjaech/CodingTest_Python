from collections import deque
def solution(cards1, cards2, goal):
    # 1. 두 리스트를 deque(큐)로 변환
    q1 = deque(cards1)
    q2 = deque(cards2)

    
    for word in goal:
        if q1 and word == q1[0]:
            word1 = q1.popleft()
        elif q2 and word == q2[0]:
            word2 = q2.popleft()
        else:
            return "No"
    
    return "Yes"