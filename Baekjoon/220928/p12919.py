# 단순히 문제처럼 읽고 구현하면 시간초과가 남
# 문제에서 더해가면서 하라 했을때 시간초과가 난다면 빼가면서 해보기
# S에서부터 두가지 경우의 수를 하나하나 해보는 것 보다 T에서부터 빼가면서 하면 경우의 수가 줄어들기 때문에 시간초과를 면할 수 있다.
import sys
sys.setrecursionlimit(100000000)
S = input()
T = input()
answer = 0
def func(S, T):
    global answer
    if len(S) > len(T):
        return
    if S == T:
        answer = 1
        return
    if T[-1] == 'A' and func(S, T[:-1]):
        answer = 1
        return
    elif T[0] == 'B' and func(S, T[:0:-1]):
        answer = 1
        return
func(S, T)
print(answer)
