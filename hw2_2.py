def cnt_tri(nums):
    n = len(nums)
    cnt = 0
    if n < 3:
        return 0
    nums.sort()
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and nums[i] + nums[j] > nums[k]:
                k += 1
            cnt += k - j - 1
    return cnt


n = int(input())
nums = list(map(int, input().split(",")))

# nums = [4, 3, 6, 7]
print(cnt_tri(nums))
