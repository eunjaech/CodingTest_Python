def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    
    while left <= right:
        mid = (left+right)//2
        
        removed = 0
        prev = 0
        
        for rock in rocks:
            if rock - prev < mid:
                removed+=1
            else:
                prev = rock
        
        if removed > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    
    return answer