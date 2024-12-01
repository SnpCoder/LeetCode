def candy(ratings: list[int]) -> int:
    n = len(ratings)
    swt = [1 for _ in range(n)]
    for i in range(1, n, 1):
        if ratings[i] > ratings[i - 1]:
            swt[i] = max(swt[i], swt[i - 1] + 1)
    for j in range(n - 1, 0, -1):
        if ratings[j - 1] > ratings[j]:
            swt[j - 1] = max(swt[j - 1], swt[j] + 1)
    return sum(swt)


ratings = [1, 0, 2]
print(candy(ratings))
