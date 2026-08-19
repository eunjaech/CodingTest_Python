def solution(array):
    answer = 0
    max_arr = []
    my_hash = {}
    for num in array:
        my_hash[num] = my_hash.get(num,0)+1
        
    max_freq = max(my_hash.values())
    modes = []
    for k, v in my_hash.items():
        if v == max_freq:
            modes.append(k)
    
    
    return modes[0] if len(modes) == 1 else -1