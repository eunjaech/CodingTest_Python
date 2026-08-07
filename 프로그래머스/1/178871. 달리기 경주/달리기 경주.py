def solution(players, callings):
    my_hash = {}
    for i in range(len(players)):
        my_hash[players[i]] = i
    for name in callings:
        current_idx = my_hash[name]
        
        prev_idx = current_idx - 1
        prev = players[prev_idx]
        
        players[current_idx], players[prev_idx] = players[prev_idx], players[current_idx]        
        my_hash[name] = prev_idx
        my_hash[prev] = current_idx
        
    return players