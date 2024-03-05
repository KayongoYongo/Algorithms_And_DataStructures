#!/usr/bin/python3

from typing import List

def majorityElement(nums: List[int]) -> int:
    """
    A function that finds the majority element in an array

    Args:
        nums (List[int])

    Returns:
        An integer which is the commonly occuring element in the list
    """
    # Initialize a dictionary to store the common occuring element
    # The key will store the number where as the value will be the frequency
    max_dict = {}

    for num in nums:
        max_dict[num] = max_dict.get(num, 0) + 1

    return max(max_dict, key=max_dict.get)

print("Example 1")
nums = [3,2,3]
print("The common element in {} is {}.".format(nums, majorityElement(nums)))

print("Example 2")
nums = [2,2,1,1,1,2,2]
print("The common element in {} is {}.".format(nums, majorityElement(nums)))
