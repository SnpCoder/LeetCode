def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""
    # char_set = set(s)
    for i, char in enumerate(s):
        if char.swapcase() not in s:
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i + 1 :])
            return left if len(left) >= len(right) else right
    return s


# 测试用例
S1 = "abABB"
S2 = "abA"
S3 = "YazaAay"

print(longestNiceSubstring(S1))  # 输出: "abABB"
print(longestNiceSubstring(S2))  # 输出: ""
print(longestNiceSubstring(S3))  # 输出: "aAa"
