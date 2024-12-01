def canJump(nums: list[int]) -> bool:
    oil = nums[0]
    step = 0
    while oil > 0 and step < len(nums) - 1:
        step += 1
        oil = max(oil - 1, nums[step])
    return step == len(nums) - 1


nums = list(map(int, input().split(",")))
print(canJump(nums))
