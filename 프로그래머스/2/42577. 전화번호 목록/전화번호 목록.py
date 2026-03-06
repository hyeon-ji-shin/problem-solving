# phone_book의 원소를 정렬하면, 가까운 숫자끼리 바로 접두어 확인이 수월해진다.

def solution(phone_book):
    phone_book.sort() # 전화번호부 정렬
    
    # 전화번호부에서 연속된 두 번호 비교
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]): # 접두어 확인을 위해 startswith() 함수를 사용한다.
            return False # 접두어인 경우가 있다면 false.
    return True