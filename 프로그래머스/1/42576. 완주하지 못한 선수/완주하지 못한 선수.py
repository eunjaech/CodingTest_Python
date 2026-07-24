def solution(participant, completion):
    my_hash = {}
    for name in participant:
        my_hash[name] = my_hash.get(name, 0) + 1
    for name in completion:
        my_hash[name] = my_hash.get(name,0) - 1
    for name in my_hash:
        if my_hash[name] == 1:
            return name
    return -1