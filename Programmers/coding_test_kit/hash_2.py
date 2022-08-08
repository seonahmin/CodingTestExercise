from itertools import combinations
def solution(nums):
    answer = 0
    set_nums = set(nums)
    if len(set_nums) <= (len(nums) // 2):
        return len(set_nums)
    elif len(set_nums) > (len(nums) // 2):
        return len(nums) // 2