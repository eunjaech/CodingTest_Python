from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
    for key in graph:
        graph[key].sort(reverse=True)
    
    st = ["ICN"]
    path = []
    
    while st:
        curr = st[-1]
        
        if curr in graph and graph[curr]:
            next_dest = graph[curr].pop()
            st.append(next_dest)
        else:
            path.append(st.pop())
        
    return path[::-1]