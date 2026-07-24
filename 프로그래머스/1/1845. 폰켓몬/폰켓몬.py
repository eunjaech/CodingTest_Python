def solution(nums):
    answer = 0
    n = len(nums)
    my_hash = {}
    for num in nums:
        my_hash[num] = my_hash.get(num,0) + 1
    half = n // 2
    if half >= len(my_hash):
        answer = len(my_hash)
    else:
        answer = half
    return answer