def solution(genres, plays):
    answer = []
    dict1, dict2 = {}, {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dict1:
            dict1[genre] = [[idx, play]]
        else:
            dict1[genre].append([idx, play])
    
        if genre not in dict2:
            dict2[genre] = play
        else:
            dict2[genre] += play

    
    for k, v in sorted(dict2.items(), key=lambda x:x[1], reverse=True):
        for idx, play in sorted(dict1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]
print (solution(genres, plays))