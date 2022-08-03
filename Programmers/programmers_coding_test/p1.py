def search(arr, x):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
    return -1

def solution(X, Y):
    x_list = sorted(list(map(int, X)))
    y_list = sorted(list(map(int, Y)))
    common = []
    for x in x_list:
        idx = search(y_list, int(x))
        if idx != -1:
            common.append(y_list[idx])
            y_list.remove(y_list[idx])
    if len(common) == 0:
        return '-1'
    common = list(map(str, common))
    common = ''.join(common[::-1])
    common = str(int(common))
    return common
