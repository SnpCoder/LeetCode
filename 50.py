def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0

    res = 1

    if n == 0 or x == 1:
        return res

    base = x
    pow = abs(n)
    while pow > 0:
        if pow % 2 == 1:
            res *= base
        base *= base
        pow //= 2

    return res if n > 0 else 1 / res


print(myPow(2.00000, -2))
