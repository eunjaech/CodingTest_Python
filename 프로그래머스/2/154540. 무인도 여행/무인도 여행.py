import sys
sys.setrecursionlimit(10**6)
def solution(maps):
    answer = []
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(r,c):
        visited[r][c] = True
        total = int(maps[r][c])
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    total += dfs(nr,nc)
        return total

    
    for r in range(rows):
        for c in range(cols):
            if maps[r][c]!='X' and not visited[r][c]:
                island = dfs(r,c)
                answer.append(island)
    answer.sort()

    
    return answer if answer else [-1]