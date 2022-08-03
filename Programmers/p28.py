'''
아이디어 : 길이 순으로 정렬한 바로 다음에 오는 집합과의 차집합을 이용해서 
새로 추가된 애들을 추가하면서 가장 마지막에 완성된 리스트를 반환하자
'''
def solution(s_list):
    answer = []
    set_list = []
    s_list = s_list[1:-1]
    for s in s_list:
        if s == '{': # 숫자 받을 준비
            str_int = [] # 숫자 담을 리스트
            tmp = [] # 튜플로 만들기 위해 완성된 숫자들을 담을 리스트
            continue
        elif s == '}':
            if len(str_int) == 1: # 받은 숫자가 한자리 일 때
                tmp.extend(str_int) # 튜플의 한 요소로 넣어줌
            else: # 받은 숫자가 한자리 수가 아닐 때
                str_int = list(map(str, str_int))
                str_int = ''.join(str_int)
                tmp.extend([int(str_int)])
            set_list.append(tmp)
            str_int = []
        elif s == ',':
            if len(str_int) == 0: # 튜플과 튜플 사이에 있는 , 일때
                continue
            else: # 하나의 튜플 안에서 값들을 나누기 위한 , 일때 
                if len(str_int) == 1:
                    tmp.extend(str_int)
                else:
                    str_int = list(map(str, str_int))
                    str_int = ''.join(str_int)
                    tmp.extend([int(str_int)])
                str_int = []
                continue
        else:
            str_int.append(int(s))
    set_list = sorted(set_list, key=lambda x : len(x)) # 길이 순으로 정렬해줌
    for s in set_list:
        if len(answer) == 0:
            answer.append(s)
        else:
            value = set(s) - set(answer[-1])
            answer.append(answer[-1]+list(value))
    return answer[-1]

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{20,111},{111}}")