from collections import deque
def solution(maps):
    answer = 0
    rows, cols = len(maps), len(maps[0])
    queue = deque([(0,0)])
    
    while queue:
        r,c = queue.popleft()
        for dr,dc in [(-1,0),(0,-1), (1,0), (0,1)]:
            nr, nc = dr + r, dc + c
            if 0<=nr<rows and 0<=nc<cols and maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1
                queue.append((nr,nc))
    answer = maps[rows-1][cols-1]
        
    return answer if answer > 1 else -1