def solution(participant, completion):
    count = {}
    
    for person in participant:
        if person in count:
            count[person] += 1
        else:
            count[person] = 1
            
    for person in completion:
        count[person] -= 1
    
    for person in count:
        if count[person] > 0:
            return person