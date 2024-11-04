import random
import heapq


def findKthLargest0(nums: list[int], k: int) -> int:
    def partition(left, right, pivot_idx):
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        return store_idx

    def quicksort(left, right, kth):
        if left == right:
            return nums[right]
        # ran_idx = random.randint(left, right)
        idx = (left + right) >> 1
        pivot_idx = partition(left, right, idx)
        if pivot_idx == kth:
            return nums[pivot_idx]
        elif pivot_idx < kth:
            return quicksort(pivot_idx + 1, right, kth)
        elif pivot_idx > kth:
            return quicksort(left, pivot_idx - 1, kth)

    return quicksort(0, len(nums) - 1, len(nums) - k)


def findKthLargest(nums: list[int], k: int) -> int:
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    return min_heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))
