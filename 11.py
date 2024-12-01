def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    maxarea = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        maxarea = max(maxarea, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxarea


height = list(map(int, input().split(",")))

print(maxArea(height))
