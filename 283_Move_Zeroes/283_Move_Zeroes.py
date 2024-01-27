#!/usr/bin/python3

import copy
from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    This function moves zeros in place
    
    Args:
        nums- An array of integers

    Return:
        None
    """
    # Initializ two empty pointers
    l, r = 0, 0

    # Iterate through the array using the right pointer
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    return nums

# Test case 1
nums = [0,1,0,3,12]
deep_copied_list = copy.deepcopy(nums)
modified = moveZeroes(nums)
print("Original list is {}. The modified list is {}.".format(deep_copied_list, modified))
