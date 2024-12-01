def quick_sort(nums: list[str]):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [x for x in nums[1:] if x + pivot > pivot + x]
    right = [x for x in nums[1:] if x + pivot <= pivot + x]
    return quick_sort(left) + [pivot] + quick_sort(right)


def largestNumber(nums: list[int]) -> str:
    nums = list(map(str, nums))
    nums = quick_sort(nums)
    result = "".join(nums).lstrip("0")
    result = result if result else "0"
    return result


nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))
