'''
다시 도전해야 하는 문제.
채점 결과
정확성: 71.4
합계: 71.4 / 100.0
'''

from collections import deque

def calc_score(score_list):
    total_score = 0
    for i, s in enumerate(score_list):
        if s > 0:
            total_score += (10 - i)
    return total_score

def solution(n, info):
    '''
        n : 화살의 개수
        info : 어피치가 맞춘 과녁 점수 개수. 10점부터 0점까지
        라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 
        가장 낮은 점수를 더 많이 맞힌 경우를 return 
    '''
    q = deque()
    start_idx = 0
    first_total_score = calc_score(info)
    apeach_score = 0 # 첫 번째에서 점수를 못 땄을 경우
    ryan_score = 0
    arrow_cnt = n
    ryan_score_cnt_list = [0 for _ in range(11)]
    q.append([start_idx, apeach_score, ryan_score, arrow_cnt, ryan_score_cnt_list])
    total_case = []
    while q:
        # 현재 점수의 인덱스, 어피치 점수, 라이언 점수, 남은 화살 수, 라이언 이긴 횟수 리스트
        idx, apeach_score, ryan_score, arrow_cnt, ryan_score_cnt_list = q.popleft()
        if arrow_cnt <= 0 or idx > 10:
            apeach_score = 0
            for i in range(len(ryan_score_cnt_list)):
                if info[i] != 0 and info[i] >= ryan_score_cnt_list[i]:
                    apeach_score += (10-i)
            if ryan_score <= apeach_score:
                continue
            else:
                if ryan_score > apeach_score:
                    if idx > 10 and sum(ryan_score_cnt_list) < n:
                        ryan_score_cnt_list[-1] = n - sum(ryan_score_cnt_list)
                    total_case.append((abs(apeach_score - ryan_score), ryan_score_cnt_list, apeach_score, ryan_score))
                continue
        # 어피치가 점수를 가져갈 때
        if info[idx] > 0:
            q.append((idx+1, apeach_score + (10 - idx), ryan_score, arrow_cnt, ryan_score_cnt_list))
        
        # 라이언이 점수를 가져갈 때
        score_list = ryan_score_cnt_list.copy()
        score_list[idx] = info[idx] + 1
        now_arrow_cnt = arrow_cnt-(info[idx] + 1)
        if now_arrow_cnt < 0:
            continue
        else:
            q.append((idx+1, apeach_score, ryan_score + (10 - idx), now_arrow_cnt, score_list))
    
    if len(total_case) == 0:
        return [-1]
    else:      
        total_case = sorted(total_case, key=lambda x:(x[0],x[::-1]), reverse=True)
        # print(total_case[:5])
    return total_case[0][1]