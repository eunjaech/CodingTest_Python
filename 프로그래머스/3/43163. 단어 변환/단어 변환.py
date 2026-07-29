from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    queue = deque([(begin,0)])
    visited = set()
    
    while queue:
        curr, idx = queue.popleft()
        if curr == target:
            return idx
        for word in words:
            if word not in visited:
                diff = 0
                for a,b in zip(curr, word):
                    if a != b:
                        diff += 1
                if diff == 1:
                    visited.add(word)
                    queue.append((word,idx+1))
            
            
    return answer