def solution(citations):
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        h_index = n - i
        if citations[i] >= h_index:
            return h_index

            
    return 0