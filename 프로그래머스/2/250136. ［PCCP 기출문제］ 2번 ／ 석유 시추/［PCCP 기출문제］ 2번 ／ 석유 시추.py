import sys
sys.setrecursionlimit(10**6)
def solution(land):
    rows = len(land)
    cols = len(land[0])
    
    visited = [[False] * cols for _ in range(rows)]
    oil_by_col = [0] * cols
    
    def dfs(r,c,visited_cols):
        visited[r][c] = True
        visited_cols.add(c)
        total = 1
        
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0<=nr<rows and 0<=nc<cols:
                if land[nr][nc] == 1 and not visited[nr][nc]:
                    total += dfs(nr,nc,visited_cols)
        return total
    
    # 전체 격자를 한 번만 순회
    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 1 and not visited[r][c]:
                visited_cols = set()
                
                size = dfs(r, c, visited_cols)
                
                # 석유 덩어리가 걸쳐있는 모든 열에 석유량 추가
                for col in visited_cols:
                    oil_by_col[col] += size
                
        
    return max(oil_by_col)