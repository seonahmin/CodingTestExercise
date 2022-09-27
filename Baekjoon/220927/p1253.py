import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
cnt = 0
for target_i in range(N):
    s = 0
    e = N-1
    while s < e:
        if s == target_i:
            s += 1
        elif e == target_i:
            e -= 1
        else:
            if arr[target_i] == arr[s] + arr[e]:
                cnt += 1
                break
            elif arr[target_i] < arr[s] + arr[e]:
                e -= 1
            else:
                s += 1
print(cnt)
    
