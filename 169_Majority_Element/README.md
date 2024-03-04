# 169. Majority Element

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n / 2` times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

`n == nums.length`
`1 <= n <= 5 * 104`
`-109 <= nums[i] <= 109`
 

Follow-up: Could you solve the problem in linear time and in `O(1)` space?

# Solution:

The **Boyer-Moore Voting Algorithm** is an efficient algorithm used to find the majority element in a given array or sequence.
The majority element is the element that appears more than n/2 times in the array, where n is the size of the array.

Here's how the Boyer-Moore Voting Algorithm works:

1. Initialize two variables: candidate and count.

 * candidate represents the current majority candidate.
 * count represents the count of occurrences of the candidate in the array.

2. Iterate through the array:

 * If count is 0, set the current element as the candidate and set count to 1.
 * If the current element is the same as the candidate, increment count.
 * If the current element is different from the candidate, decrement count.
 
3. At each iteration, check if count becomes 0. If it does, update the candidate to the current element and set count to 1 again.

4. After iterating through the entire array, the candidate will represent the potential majority element.
   However, we need to perform a second pass through the array to verify if the candidate is indeed the majority element by counting its occurrences.
   If it appears more than n/2 times, then it's the majority element; otherwise, there's no majority element.

Conditions to use the Boyer-Moore Voting Algorithm:

1. The algorithm assumes that there is always a majority element in the array.
2. It works efficiently when the majority element appears more than n/2 times in the array.
3. The algorithm requires a linear pass through the array, making it quite efficient with O(n) time complexity.
4. It doesn't require extra space except for two variables (candidate and count), making it a space-efficient algorithm.
Overall, the Boyer-Moore Voting Algorithm is a handy technique for finding the majority element in an array with a simple and efficient approach.
