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
    # Initializ an empty pointer
    non_zero = 0

    # The purpose of the above pointer is to store the position of the next non zero element

    # Iterate through the array using the right pointer
    for i in range(len(nums)):
        if nums[i] != 0:
            # Carry out a swap operation
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            # This stores the position of the next non zero element
            non_zero += 1

    return nums

# Test case 1
nums = [0,1,0,3,12]
deep_copied_list = copy.deepcopy(nums)
modified = moveZeroes(nums)
print("Original list is {}. The modified list is {}.".format(deep_copied_list, modified))
