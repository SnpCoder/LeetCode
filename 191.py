def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += 1 if n & 0x1 else 0
        n >>= 1
    return count


# Brian Kernighan 算法
def hammingWeight1(n: int) -> int:
    count = 0
    while n:
        n &= (
            n - 1
        )  # 从数 n 中减去 1，会在二进制中产生一个变化，具体表现为最低位的 1 变成 0，而它后面的所有位变为 1。
        count += 1
    return count


print(hammingWeight1(2147483645))
