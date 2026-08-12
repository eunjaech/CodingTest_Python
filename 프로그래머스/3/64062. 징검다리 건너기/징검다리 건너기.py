def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left+right)//2
        
        zero_count = 0 
        possible = True
        
        for stone in stones:
            if stone < mid:
                zero_count+=1
                if zero_count >= k:
                    possible = False
                    break
            else:
                zero_count = 0
        if possible:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer