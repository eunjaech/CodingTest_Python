def solution(d, budget):
    d.sort()
    answer = 0
    left, right = 1, len(d)
    
    while left <= right:
        mid = (left+right)//2
        
        total = sum(d[:mid])
        
        if total <= budget:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer