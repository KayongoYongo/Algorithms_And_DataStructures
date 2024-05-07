
#!/usr/bin/python3
from typing import List

def removeEvenNumbers(nums: List[int]) -> List[int]:
    """
    Description:
        This function removes even numbers from a list
    
    Args:
        nums: A list of integers

    Return:
        A list without even numbers
    """
    # Main idea is to solve the equation with constant space of 0(1) instead of 0(n)
    # We need a value to store the position of the next even element
    even = 0
    # We need to iterate through the array
    for i in range(len(nums)):
        # Checks if the element is divisible by 2
        if nums[i] % 2 == 0:
            # Switch the elements
            nums[i], nums[even] = nums[even], nums[i]
            # Store the position of the next even element
            even += 1
    # Print the number of the element after modification
    print(even)
    # Since we want the array without the even elements, I'll perform list slicing
    return nums[even:]

nums = [1,2,3,5,8,9]
# Print the list

print(f"The modified list is {removeEvenNumbers(nums)}")