from collections import deque

def extract_pieces(board, target_val):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    pieces = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target_val and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                piece = [(i, j)]
                while q:
                    x, y = q.popleft()
                    
                    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == target_val and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))  
                                piece.append((nx, ny))
                # 추출한 조각을 (0,0) 기준으로 정규화하여 저장
                pieces.append(normalize(piece))
                
    return pieces

def normalize(piece):
    min_x = min(p[0] for p in piece)
    min_y = min(p[1] for p in piece)
    
    normalized = [(x - min_x, y - min_y) for x, y in piece]
    
    return sorted(normalized)

def rotate(piece):
    rotated = [(y, -x) for x, y in piece]
    return normalize(rotated)

def solution(game_board, table):
    # 1. game_board의 빈 공간(0)들과 table의 퍼즐 조각(1)들 추출
    spaces = extract_pieces(game_board, 0)
    blocks = extract_pieces(table, 1)
    
    answer = 0
    used_spaces = [False] * len(spaces)
    
    # 2. 각 퍼즐 블록마다 보드의 빈 공간과 맞춰보기
    for block in blocks:
        matched = False
        for i, space in enumerate(spaces):
            if used_spaces[i]:
                continue
            if len(block) != len(space):
                continue
                
            curr_block = block
            for _ in range(4):
                if curr_block == space:
                    used_spaces[i] = True
                    answer += len(block)  # 맞춘 칸 수 더하기
                    matched = True
                    break
                curr_block = rotate(curr_block)
            if matched:
                break
    return answer