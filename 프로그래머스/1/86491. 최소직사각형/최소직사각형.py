def solution(sizes):
    height, width = 0,0
    for h,w in sizes:
        long_side = max(h,w)
        short_side = min(h,w)
        
        height = max(height, long_side)
        width = max(width, short_side)
        
        
    return height * width