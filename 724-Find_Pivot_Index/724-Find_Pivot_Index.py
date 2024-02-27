#!/usr/bin/python3

from typing import List

def pivotIndex(nums: List[int]) -> int:
    """
    This function returns the pivot index

    Args:
        nums: A list

    Return:
        0, 1 or the pivot index
    """
    left_sum = 0
    total = sum(nums)

    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i
        left_sum += nums[i]
    return -1

nums = [1,7,3,6,5,6]
print("The pivot index of {} is {}.".format(nums, pivotIndex(nums)))
nums = [1,2,3]
print("The pivot index of {} is {}.".format(nums, pivotIndex(nums)))
nums = [2,1,-1]
print("The pivot index of {} is {}.".format(nums, pivotIndex(nums)))
