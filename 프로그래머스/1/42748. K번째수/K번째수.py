def solution(array, commands):
    answer = []
    for i,j,k in commands:
        key = sorted(array[i-1:j])
        answer.append(key[k-1])
    return answer