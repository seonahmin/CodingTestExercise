def check_right(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True

def split_uv(s):
    u, v = '', ''

    for i in range(2, len(s)+1, 2):
        if s[:i].count('(') == s[:i].count(')'):
            u = s[:i]
            v = s[i:]
            break
    return u, v

def change_balance_string(inputs):
    answer = ''
    if len(inputs) == 0:
        return inputs
    u, v = split_uv(inputs)
    if check_right(u):
        answer += u
        answer += change_balance_string(v)
    else:
        answer += '('
        answer += change_balance_string(v)
        answer += ')'
        list_trimmed_u = list(u[1:-1])
        flipped_u = list(map(lambda x : ')' if x == '(' else '(', list_trimmed_u))
        str_u = ''.join(flipped_u)
        answer += str_u
    
    return answer

def solution(p):
    answer = ''
    answer = change_balance_string(p)
    return answer

solution("()))((()")