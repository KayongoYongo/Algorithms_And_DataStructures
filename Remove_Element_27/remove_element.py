#!/usr/bin/python3

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums[:]:
            if num == val:
                nums.remove(val)

        return len(nums)

# Test data
test_solution = Solution()

# Test Case 1
nums1 = [3, 2, 2, 3]
val1 = 3
result1 = test_solution.removeElement(nums1, val1)
print(f"Input: nums = {nums1}, val = {val1}\nOutput: {result1}, nums = {nums1}")

# Test Case 2
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
result2 = test_solution.removeElement(nums2, val2)
print(f"Input: nums = {nums2}, val = {val2}\nOutput: {result2}, nums = {nums2}")

# Test Case 3
nums3 = [1, 2, 3, 4, 5]
val3 = 3
result3 = test_solution.removeElement(nums3, val3)
print(f"Input: nums = {nums3}, val = {val3}\nOutput: {result3}, nums = {nums3}")
