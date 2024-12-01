def getPermutation(n: int, k: int) -> str:
    result = []
    nums = [i for i in range(1, n + 1, 1)]

    def back_tracking(path, remaining):
        if not remaining:
            result.append(path)
            return
        for i in range(len(remaining)):
            back_tracking(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])
        return

    back_tracking([], nums)
    res = "".join(list(map(str, result[k - 1])))

    return res


# 康托展开
def getPermutation2(n: int, k: int) -> str:
    result = ""
    nums = [i for i in range(1, n + 1, 1)]
    fac = [1] * n
    for i in range(1, n):
        fac[i] = fac[i - 1] * i

    k -= 1
    for j in range(n, 0, -1):
        idx = k // fac[j - 1]
        k %= fac[j - 1]
        result += str(nums[idx])
        nums.pop(idx)
    return result
