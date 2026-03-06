def solution(phone_book):
    answer = True
    
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1  # 딕셔너리에서 키 존재 여부 확인 : O(1)
        
        # phone_book = ["119", "97674223", "1195524421"]
        
        # to
        
        # {
        #  "119":1,
        #  "97674223":1,
        #  "1195524421":1
        # }
    
    # 전화번호부에서 번호 하나 꺼내서
    for phone_number in phone_book:
        temp = ""
        # 한글자씩 끊어서 hash_map에 있는 다른 번호(접두어인 경우)에 해당하는 지 확인 (자기 자신 제외)
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
                
    return answer