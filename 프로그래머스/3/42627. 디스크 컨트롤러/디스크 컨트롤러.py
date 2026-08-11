import heapq
def solution(jobs):
    heap = []
    jobs.sort(key=lambda x: x[0])
    current, total, count = 0,0,0
    i = 0
    n = len(jobs)
    
    while count < n:
        # 현재 시각 이하에 요청된 모든 작업을 힙에 추가
        while i < n and jobs[i][0] <= current:
            heapq.heappush(heap,[jobs[i][1],jobs[i][0]])
            i+=1
        if heap:
            #대기 중인 작업이 있으면 소요 시간이 가장 짧은 것부터 처리
            duration, request_time = heapq.heappop(heap)
            current += duration
            total += (current-request_time)
            count+=1
            
        else:
            #대기 중인 작업이 없으면 디스크가 쉼 -> 다음 작업의 요청 시점으로 이동
            current = jobs[i][0]
    return total // n