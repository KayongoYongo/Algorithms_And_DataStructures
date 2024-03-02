#!/usr/bin/python3

def max_subarray_sum(nums):
    """
    This function finds the maximum
    sub array within a list of 3 integers

    Args:
        nums: The array to be vetted

    Return:
        The value of the max array
    """
    # initialize the sum of the first window sum
    window_sum = sum(nums[:3])

    # Initialize the first max sum
    max_sum = window_sum

    # Iterate through the array using the for looop
    for i in range(3, len(nums)):
        # Update the sum of the window by adding the left and right pointer
        window_sum = window_sum + nums[i] - nums[i - 3]
        # Update the max sum
        max_sum = max(max_sum, window_sum)

    return max_sum


nums = [1, 3, -1, -3, 5, 3, 6, 7]
print("Example 1:")
print(nums)
print("The max sub array is {}".format(max_subarray_sum(nums)))
