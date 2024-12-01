def has_intersection(a: list[int], b: list[int]):
    return max(a[0], b[0]) <= min(a[1], b[1])


def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    arrow = 1
    cur_end = points[0][1]
    for lst in points:
        if lst[0] > cur_end:
            arrow += 1
            cur_end = lst[1]
    return arrow


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShots(points))
