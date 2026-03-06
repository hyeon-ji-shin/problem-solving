# 동일한 종류의 폰켓몬을 뽑으면 하나로 처리되므로, set을 이용해서 중복 사전처리
def solution(nums):
    num_set = set(nums) # 중복 제외한 폰켓몬 총 종류 갯수
    n = len(nums)       # 전체 폰켓몬 수
    k = n // 2          # 뽑아야 하는 폰켓몬 수
    
    # e.g. 뽑아야 하는 폰켓몬 수(k) <= num_set : 가능한 최대 폰켓몬 종류(answer) == 뽑아야 하는 폰켓몬 수(k)가 됨.
    return min(k, len(num_set))