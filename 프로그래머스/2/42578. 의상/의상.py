def solution(clothes):
    answer = 1
    my_hash = {}
    for i, clothe in clothes:
        my_hash[clothe] = my_hash.get(clothe,0)+1
    for clothe in my_hash:
        answer *= (my_hash[clothe]+1)
    
    return answer-1