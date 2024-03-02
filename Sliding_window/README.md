# Sliding window algorithm

## Introduction
The sliding window algorithm is a technique used for finding subarrays or substrings within a larger array or string that satisfy certain criteria.
It involves defining a window (a range of elements or characters) and then moving that window across the array or string, 
examining the elements or characters within the window at each step.

# Explanation
Here's a step-by-step explanation of the sliding window algorithm:

**Initialization:** 
Set up two pointers, usually named "left" and "right", to define the boundaries of the initial window.
These pointers typically start at the beginning of the array or string.

**Move the Window:**
Move the right pointer to expand the window, adding elements or characters to it.
At each step, check if the current window satisfies the required criteria.
If it does, update the result accordingly. If not, keep expanding the window.

**Adjust the Window:**
Once the window satisfies the criteria or cannot be expanded further, move the left pointer to shrink the window, 
removing elements or characters from it. Again, check if the current window satisfies the criteria.
If it does, update the result accordingly. If not, keep shrinking the window.

**Repeat:** 
Continue steps 2 and 3 until the right pointer reaches the end of the array or string.

Example:
Find themaximum sum of a sub array of size 3.
Array = [1, 3, -1, -3, 5, 3, 6, 7] , k = 3
