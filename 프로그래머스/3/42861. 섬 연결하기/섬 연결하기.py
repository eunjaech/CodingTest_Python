def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    # 이미 연결된 섬들을 담는 집합 (첫 번째 다리의 한쪽 섬으로 시작)
    connected = {costs[0][0]}
    total_cost = 0
    
    while len(connected) < n:
        for u, v, cost in costs:
            # 두 섬 중 하나만 연결된 집합에 포함되어 있을 때만 다리를 건설 (사이클 방지)
            if u in connected and v in connected:
                continue
            if u in connected or v in connected:
                connected.add(u)
                connected.add(v)
                total_cost += cost
                break
    return total_cost
                
    
        
    return answer