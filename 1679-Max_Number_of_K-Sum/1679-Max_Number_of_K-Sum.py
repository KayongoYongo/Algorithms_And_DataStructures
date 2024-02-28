#!/usr/bin/python3

from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    # 1. Sort the array in ascending order
    nums.sort()

    # 2. Initialize two ponters and a counter
    left, right = 0, len(nums) - 1
    count = 0

    # 3 . Iterate through the list 
    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == k:
            count += 1
            # 4. Perform the 'delete operation'
            left += 1
            right -= 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return count
