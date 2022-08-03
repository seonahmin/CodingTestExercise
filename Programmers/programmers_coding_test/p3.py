from collections import deque
def solution(order):
    answer = 0
    original = deque([1,2,3,4,5]) # 정렬된 택배들
    tmp = [] # 보조컨베이어
    rst = []
    idx = 0
    while idx < 5:
        if len(original) > 0:
            if order[idx] != original[0]:
                if len(tmp) > 0:
                    if tmp[-1] == order[idx]:
                        rst.append(tmp.pop())
                        idx += 1
                    else:
                        tmp.append(original.popleft())
                else:
                    tmp.append(original.popleft())
            else:
                rst.append(original.popleft())
                idx += 1
        else:
            if len(tmp) > 0:
                if tmp[-1] == order[idx]:
                    rst.append(tmp.pop())
                    idx += 1
                else:
                    break   
            else:
                break
    answer = len(rst)
    return answer