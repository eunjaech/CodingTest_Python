def solution(sizes):
    answer = 0
    height, width = 0,0
    for h,w in sizes:
        temp = max(h,w)
        temp2 = min(h,w)
        hw = max(height,width)
        if temp >= hw:
            height = temp
        if temp2 >= width:
            width = temp2
        
    answer = height * width
        
        
    return answer