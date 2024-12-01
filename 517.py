def findMinMoves(machines: list[int]) -> int:
    n = len(machines)
    total = sum(machines)
    if total % n != 0:
        return -1
    avg = total // n
    diff_sum = 0
    max_op = 0
    for cloth in machines:
        diff = cloth - avg
        diff_sum += diff
        max_op = max(max_op, abs(diff_sum), diff)
    return max_op
