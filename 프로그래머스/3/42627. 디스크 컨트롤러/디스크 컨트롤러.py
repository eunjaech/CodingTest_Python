import heapq
def solution(jobs):
    heap = []
    jobs.sort(key=lambda x: (x[0]) )
    curr,total,count = 0,0,0
    i = 0
    n = len(jobs)
    
    while count < n:
        while i < n and jobs[i][0] <= curr:
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i+=1
        if heap:
            duration, request_time = heapq.heappop(heap)
            curr += duration
            total += (curr - request_time)
            count+=1
        else:
            curr = jobs[i][0]
            
        
    return total // n