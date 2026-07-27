from itertools import permutations
def solution(k, dungeons):
    max_count = 0
    for p in permutations(dungeons):
        curr_k = k
        cnt = 0
        
        for min_req, consume in p:
            if curr_k >= min_req:
                curr_k -= consume
                cnt += 1
            else:
                break
                
        max_count = max(cnt, max_count)
        
    return max_count