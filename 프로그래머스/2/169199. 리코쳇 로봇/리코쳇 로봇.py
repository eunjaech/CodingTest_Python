from collections import deque
def solution(board):
    rows = len(board)
    cols = len(board[0])
    start_r, start_c = -1,-1
    move = 0 
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start_r, start_c  = r,c
                break;
            if start_r != -1:
                break
    
    queue = deque([(start_r,start_c, move)])
    visited = [[False] * cols for _ in range(rows)]
    visited[start_r][start_c] = True
    
    while queue:
        r,c,move = queue.popleft()
        
        if board[r][c] =='G':
            return move
        
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr, nc = r, c
            while True:
                next_r = nr + dr
                next_c = nc + dc
                if not (0<=next_r<rows and 0<=next_c<cols) or board[next_r][next_c] =='D':
                    break;
                nr, nc = next_r, next_c
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr,nc, move+1))
                
            
                
                
    return -1