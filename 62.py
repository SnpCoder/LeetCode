def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)


def uniquePaths2(m: int, n: int) -> int:
    a = m + n - 2
    b = min(m, n) - 1
    top, down = 1, 1
    for i in range(a, a - b, -1):
        top *= i
    for j in range(1, b + 1, 1):
        down *= j
    return top // down


print(uniquePaths2(3, 7))
