def solution(numbers, hand):
    answer = ''
    pad = {1:(0,0), 2:(0,1),3:(0,2),
          4:(1,0), 5:(1,1), 6:(1,2),
          7:(2,0), 8:(2,1), 9:(2,2),
          '*': (3,0), 0:(3,1), '#':(3,2)}
    left = pad['*']
    right = pad['#']
    
    for num in numbers:
        if num in [1,4,7]:
            answer+='L'
            left=pad[num]
        elif num in [3,6,9]:
            answer+='R'
            right=pad[num]
        else:
            target = pad[num]
            
            #manhattan dist
            left_dist=abs(target[0]-left[0])+abs(target[1]-left[1])
            right_dist=abs(target[0]-right[0])+abs(target[1]-right[1])
            
            if left_dist < right_dist:
                answer+='L'
                left=target
            elif right_dist < left_dist:
                answer+='R'
                right=target
            else:
                if hand == "left":
                    answer+='L'
                    left=target
                else:
                    answer+='R'
                    right=target
                    
    
    return answer