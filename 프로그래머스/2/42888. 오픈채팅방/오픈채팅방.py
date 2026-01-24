def solution(record):
    userdata = {}

    # 유저 닉네임이 바뀌는 조건 : Enter, Change (Leave 제외)
    for line in record:
        cmd = line.split(" ")
        if cmd[0] != "Leave":
            userdata[cmd[1]] = cmd[2]
    
    # 최종 메세지 출력
    answer = []
    for line in record:
        cmd = line.split(" ") #문자열에서 " "기준으로 split
        if cmd[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % userdata[cmd[1]])
        elif cmd[0] == "Leave":
            answer.append("%s님이 나갔습니다." % userdata[cmd[1]])
            
    return answer