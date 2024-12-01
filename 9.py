def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverse_num = 0

    while reverse_num < x:
        reverse_num = reverse_num * 10 + x % 10
        x = x // 10
    return x == reverse_num or reverse_num // 10 == x


print(isPalindrome(121))
