def findmaxrec(h, left, right):
    if right < left:
        return 0
    min_height = h[left]
    min_idx = left
    for i in range(left, right + 1):
        if h[i] < min_height:
            min_height = h[i]
            min_idx = i
    all_area = min_height * (right + 1 - left)
    left_area = findmaxrec(h, left, min_idx - 1)
    right_area = findmaxrec(h, min_idx + 1, right)
    return max(all_area, left_area, right_area)


n = int(input())
heights = list(map(int, input().split()))

res = findmaxrec(heights, 0, n - 1)

print(res)
