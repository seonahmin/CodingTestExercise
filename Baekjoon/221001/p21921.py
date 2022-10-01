import sys
N, X = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
sum_arr = [0 for _ in range(len(arr))]
sum_arr[0] = arr[0]
for i in range(1, len(arr)):
    sum_arr[i] = sum_arr[i-1] + arr[i]
max_val = 0
day_cnt = 0
for i in range(X-1, len(sum_arr)):
    if i - X < 0:
        val = sum_arr[X-1]
        if max_val < val:
            max_val = val
            day_cnt = 1
    else:
        val = sum_arr[i] - sum_arr[i-X]
        if max_val < val:
            max_val = val
            day_cnt = 1
        elif max_val == val:
            day_cnt += 1
if max_val>0:
    print(max_val)
    print(day_cnt)
else:
    print('SAD')