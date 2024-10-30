def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if candidate == num else -1
    return candidate


testcase = [2, 2, 1, 1, 1, 2, 2]

print(majorityElement(testcase))

# 摩尔投票法
