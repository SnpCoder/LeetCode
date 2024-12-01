def maxSubArray(nums: list[int]) -> int:
    n = len(nums)
    cur_sum = max_sum = nums[0]
    for i in range(1, n):
        cur_sum = max(cur_sum + nums[i], nums[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum
