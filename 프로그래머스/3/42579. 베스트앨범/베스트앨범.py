def solution(genres, plays):
    answer = []
    total_hash = {}
    song_hash = {}
    
    for i in range(len(genres)):
        g,p = genres[i], plays[i]
        total_hash[g] = total_hash.get(g,0)+p
        
        if g not in song_hash:
            song_hash[g] = []
        song_hash[g].append((i,p))
    
    sorted_total = sorted(total_hash, key=lambda x: total_hash[x], reverse=True)

    for g in sorted_total:
        songs = sorted(song_hash[g], key=lambda x: (-x[1],x[0]))
        for i,song in songs[:2]:
            answer.append(i)
        
    return answer