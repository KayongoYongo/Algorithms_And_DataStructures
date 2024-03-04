#!/usr/bin/python3

from typing import List

def majorityElement(nums: List[int]) -> int:
    """
    Description: This function takes in an array
    and returns the majority

    Args:
        nums: The array containing the elements

    Return:
        The most common occuring element in the list.
    """
    # Create two separate variables
    candidate = None # Represents the current majority element
    count = 0 # Counts the occurences of candidate in the array

    # Iterate through the array
    for num in nums:
        if count == 0:
            # Reassign the value of candidate and reset count
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print("Example 1")
nums = [3,2,3]
print("The common element in {} is {}.".format(nums, majorityElement(nums)))

print("Example 2")
nums = [2,2,1,1,1,2,2]
print("The common element in {} is {}.".format(nums, majorityElement(nums)))
