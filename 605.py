def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    idx = 0
    while idx < len(flowerbed):
        if n == 0:
            return True
        if (
            flowerbed[idx] == 0
            and (idx == 0 or flowerbed[idx - 1] == 0)
            and (idx == len(flowerbed) - 1 or flowerbed[idx + 1] == 0)
        ):
            n -= 1
            idx += 2
        else:
            idx += 1
    return n == 0


flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
print(canPlaceFlowers(flowerbed, n))
