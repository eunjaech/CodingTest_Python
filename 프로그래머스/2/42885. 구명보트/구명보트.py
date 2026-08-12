def solution(people, limit):
    people.sort()
    answer = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if people[left] + people[right]<=limit:
            left+=1 # 가벼운 사람도 태움
        # 무거운 사람은 어떤 경우든 보트에 탑승함
        right-=1 
        answer+=1
        
    return answer