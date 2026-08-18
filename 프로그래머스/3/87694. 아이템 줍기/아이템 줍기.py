from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for _ in range(102)] 
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x : x * 2,r) 
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1

    #BFS 
    cx, cy =characterX * 2 , characterY * 2
    ix, iy = itemX * 2 , itemY * 2
    
    q = deque([(cx, cy)])
    visited = [[0] * 102 for _ in range(102)]
    
    visited[cx][cy] = 1
    
    while q:
        x,y = q.popleft()
        
        if x == ix and y == iy:
            return (visited[x][y] - 1) // 2
        
        for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx, ny = dx + x , dy + y
            if 0 <= nx < 102 and 0 <= ny <102:
                if field[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

    return 0