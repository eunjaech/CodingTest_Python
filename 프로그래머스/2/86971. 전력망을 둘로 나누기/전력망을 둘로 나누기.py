from collections import deque, defaultdict

def count_nodes(start, disabled_wire, graph, n):
    # 1. Fasle 오타 수정 및 len(graph) 대신 n 사용
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    cnt = 1
    u_cut, v_cut = disabled_wire
    
    while queue:
        curr = queue.popleft()
        
        for next_node in graph[curr]:
            # 2. nxt -> next_node로 변수명 수정
            if (curr == u_cut and next_node == v_cut) or (curr == v_cut and next_node == u_cut):
                continue
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                cnt += 1
    return cnt

def solution(n, wires):
    # 3. defaultdict([]) -> defaultdict(list) 수정
    graph = defaultdict(list)
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    min_diff = float('inf')
    
    for wire in wires:
        cnt = count_nodes(wire[0], wire, graph, n)
        diff = abs(2 * cnt - n)
        min_diff = min(min_diff, diff)
        
    return min_diff