def jump(nums: list[int]) -> int:
    maxpos, end = 0, 0
    jumptime = 0
    n = len(nums)
    if n == 1:
        return 0
    for i in range(n):
        maxpos = max(maxpos, i + nums[i])
        if i == end:
            jumptime += 1
            end = maxpos
            if end >= n - 1:
                return jumptime


nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
print(jump(nums))
