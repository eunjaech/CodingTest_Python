def solution(word):
    # 각 자릿수별로 모음이 바뀔 때 넘어가게 되는 단어의 개수 (가중치)
    #1+5+25+125+625
    weights = [781,156,31,6,1]
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer =  0
    for i, char in enumerate(word):
        answer += vowels[char] * weights[i] + 1
    return answer