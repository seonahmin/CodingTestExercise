# 아이디 별로 저장을 하고 아이디를 그 아이디의 닉네임으로 바꿔줄 심산
from collections import defaultdict
def solution(record):
    return_list = []
    answer = []
    user_info = defaultdict()
    for r in record:
        info = r.split(' ')
        if len(info) == 2:
            uid = info[1]
            return_list.append(f'{uid}님이 나갔습니다.')
        elif len(info) == 3:
            status = info[0]
            uid = info[1]
            name = info[2]
            if status == 'Enter':
                user_info[uid] = name 
                return_list.append(f'{uid}님이 들어왔습니다.')
            elif status == 'Change':
                user_info[uid] = name
    
    for r in return_list:
        uid, notice = r.split('님이')
        uid = user_info[uid]
        ans = [uid, notice]
        answer.append('님이'.join(ans))

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))