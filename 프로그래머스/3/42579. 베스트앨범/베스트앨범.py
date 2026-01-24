def solution(genres, plays):
    genres_dict = {}  # 장르별 곡 정보 저장하는 딕셔너리 { 장르: [(고유번호, 재생수), ...]}
    genres_rank = {}  # 많이 재생된 장르 계산하는 딕셔너리 { 장르: 총재생수 }
    
    # 1. 장르별 총 재생 횟수와 각 곡의 재생 횟수 저장
    for i in range(len(genres)): # 인덱스 사용 -> range
        # i번째 노래의 장르와 재생 횟수
        genre = genres[i]
        play = plays[i]
        
        if genre not in genres_dict:
            genres_dict[genre] = []
            genres_rank[genre] = 0
        genres_dict[genre].append((i, play))
        genres_rank[genre] += play
    
    # 2. 총 재생 횟수가 많은 장르순으로 정렬
    # sorted_genres = [("pop", 3100), ("classic", 1450)]
    sorted_genres = sorted(
        genres_rank.items(), # [("classic", 1450), ("pop", 3100)]
        key=lambda x: x[1],  # x = ("classic", 1450), x[0] = "classic", x[1] = 1450
        reverse=True # 내림차순
    )
    
    # 3. 각 장르에서 재생 횟수 상위 2곡까지 출력
    answer = []
    for genre, _ in sorted_genres:
        sorted_songs = sorted(
            genres_dict[genre], # [(4, 2500), (1, 600)]
            key=lambda x: (-x[1], x[0]) # x[1] (재생 횟수) 내림차순 -> 재생 횟수가 같으면 x[0] (고유번호) 오름차순
        )
        # 상위 2곡만, (idx, play)에서 idx만 추출
        answer.extend([idx for idx, _ in sorted_songs[:2]])
    
    return answer