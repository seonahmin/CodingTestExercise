import sys
from collections import Counter
q = []
N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
for i in range(N):
    q.append(int(input()))
answer = 0
for start_pt in range(N):
    dish = []
    if start_pt + k > N:
        dish += q[start_pt:] + q[:start_pt + k - N]
    else:
        dish += q[start_pt:start_pt+k]
    dish += [c]
    answer = max(len(Counter(dish)), answer)
print(answer)