def solution(answers):
    answer = []
    c1,c2,c3 = 0,0,0
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if (p1[i%len(p1)] == answers[i]):
            c1 += 1
        if (p2[i%len(p2)] == answers[i]):
            c2 += 1
        if (p3[i%len(p3)] == answers[i]):
            c3 +=1
    if c1 == max(c1,c2,c3):
        answer.append(1)
    if c2 == max(c1,c2,c3):
        answer.append(2)
    if c3 == max(c1,c2,c3):
        answer.append(3)
            
    return answer