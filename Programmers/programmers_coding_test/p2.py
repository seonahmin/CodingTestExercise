from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    want_info = defaultdict()
    for w, n in zip(want, number):
        want_info[w] = n
    for i in range(len(discount)-10+1):
        false_return = False
        pass_num = 0
        discount_list = discount[i:i+10]
        for w_k, w_n in want_info.items():
            if discount_list.count(w_k) < w_n:
                false_return = True
                break
        if not false_return:
            answer += 1
        

    return answer