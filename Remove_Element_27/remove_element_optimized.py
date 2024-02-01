#!/usr/bin/python3
"""
This is the most optimized solution
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        This function takes an element that exists
        and returns the number of occurences of that element
        in the list
        """
        left_ptr = 0

        for right_ptr in range(len(nums)):
            if nums[right_ptr] != val:
                nums[left_ptr] = nums[right_ptr]
                left_ptr += 1
        
        return left_ptr

# Test Case 1
nums1 = [3, 2, 2, 3]
val1 = 3
solution1 = Solution()
output1 = solution1.removeElement(nums1, val1)
print(f"Test Case 1 - Output: {output1}, nums: {nums1[:output1]}")
