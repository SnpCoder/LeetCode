def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    diff = [x - y for x, y in zip(gas, cost)]
    if sum(diff) < 0:
        return -1
    min_diff = float("inf")
    total_diff = 0
    n = len(gas)
    idx = -1
    for i in range(n):
        total_diff += diff[i]
        if min_diff > total_diff:
            min_diff = total_diff
            idx = i
    return (idx + 1) % n


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))
