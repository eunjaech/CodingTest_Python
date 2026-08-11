import heapq
def solution(operations):
    heap = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        
        if op == "I":
            heapq.heappush(heap,num)
        else:
            if heap:
                if num == -1:
                    heapq.heappop(heap)
                elif num == 1:
                    heap.remove(max(heap))
                    heapq.heapify(heap)
                    
    if not heap:
        return [0,0]
    return [max(heap),heap[0]]