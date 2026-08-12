def solution(name):
    answer = 0
    n = len(name)
    up_down = 0
    for char in name:
        up_down += min(ord(char) - ord('A'), ord('Z')-ord(char)+1 )
    
    left_right = n - 1
    i = 0
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        left_right = min(left_right, 2*i+(n-next_i), 2*(n-next_i)+i)
        
    return left_right + up_down