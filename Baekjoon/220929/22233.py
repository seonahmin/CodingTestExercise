# 시간초과가 난 코드
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
keywords = {}
for i in range(N):
    kw = input()
    keywords[kw] = 1

remain = N
for i in range(M):
    memo = sys.stdin.readline().rstrip().split(',')
    for j in memo:
        try:
            if keywords[j] != 0:
                keywords[j] -= 1
                remain -= 1
        except:
            continue
    print(remain)

# 이진탐색을 사용한 코드
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
keywords = {}
for i in range(N):
    kw = input()
    keywords[kw] = 1

for i in range(M):
    memo = sys.stdin.readline().rstrip().split(',')
    for j in memo:
        try:
            keywords[j] -= 1
        except:
            continue
    cnt = len([k for k, v in keywords.items() if v > 0])
    print(cnt)