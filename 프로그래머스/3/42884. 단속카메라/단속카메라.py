def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    cam_pos = -30001
    
    for entry, exit in routes:
        if entry > cam_pos:
            answer+=1
            cam_pos = exit
    return answer