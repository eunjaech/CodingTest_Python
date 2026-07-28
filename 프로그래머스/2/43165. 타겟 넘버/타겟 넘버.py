from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque([(0,0)])
    
    while queue:
        curr,idx = queue.popleft()
        if idx == len(numbers):
            if curr == target:
                answer+=1
        else:
            queue.append((curr+numbers[idx],idx+1))
            queue.append((curr-numbers[idx],idx+1))
        
    return answer