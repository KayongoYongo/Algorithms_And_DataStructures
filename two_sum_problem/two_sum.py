#!/usr/bin/python3
"""
This script attempts to solve the two sum solution 
by using the two pointer approach
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This solution only works if the list
        is sorted in ascending order
        """
        left, right = 0, len(nums)-1

        for _ in range(len(nums)):
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left, right]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        return None

# Test Case 1: Basic case with a valid solution
nums1 = [2, 7, 11, 15]
target1 = 9
# The solution should be indices [0, 1] as nums[0] + nums[1] = 2 + 7 = 9
print(Solution().twoSum(nums1, target1))  # Output: [0, 1]
