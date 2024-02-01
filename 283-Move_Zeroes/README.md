# Leecode Problem: 283. Move Zeroes

Given an integer array `nums`, move all `0's` to the end of it while maintaining the relative order of the non-zero elements.

***Note that you must do this in-place without making a copy of the array.***

# The problem
This question requires us to move all zeros to the end which is quite straight forward. This can be solved easily by
iterating though the array, filter out the zero and non zeo elements to differnt arrays and then append the array 
containing the zero elements at the end of the array. This would have been an easier apporach. However, the question
requires us to do the movement in place. If we think about it, this would be efficient since the arrays would take up
space in memory. Therefore, this solution would have the space complexity of 0(1).

# Things to consider:
The problem gives us various challenges:
 * Moving the elements in place
 * Using the two pointer approach to solve it.

# Solution
To solve this problem, I prefer to use the two pointer approach.

1. Intitialize two pointers, l`left` and r`right`. The purpose of the left pointer is to store the position of the non zero element
where as the purpose of the right pointer is to navigate through the list.
2. Using the right pointer navigate through the list.
3. If the element found on the index of the right pointer is zero, it is skipped. Otherwise, if it s non zero, the value of the left 
and right pointers are swapped and the left pointer is incrimented by `+1`
4. Finally the modified array is returned.

example:
``` Python
l, r = 0, 0

for r in range(nums)
	if num[r] != 0:
		nums[l], nums[r] = nums[r], nums[l]
		l += 1
return nums
```
