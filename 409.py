def longestPalindrome(s: str) -> int:
    se = set()
    l = 0
    for c in s:
        if c not in se:
            se.add(c)
        else:
            se.remove(c)
            l += 2
    return l + bool(se)


print(longestPalindrome("abccccdd"))
