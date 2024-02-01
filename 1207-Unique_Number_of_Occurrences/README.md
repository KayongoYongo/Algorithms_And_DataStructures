# 1207. Unique Number of Occurrences

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique** or `false` otherwise.

# Thoughts on the problem
This problem requires us to count the number of occurences of a number in the `arr` list. If there are unique occurences for a number,
return `Tue`. Otherwise, return `False`.

# Things to consider
1. I have to find a way of storing the number of unique occurences of the numbers in the `arr` list.
2. A `dictionary` seems like the best data structure to use to solve this core problem.
3. I have to create a list of the values and check whether there are unique values or not.

# The solution
1. Create an empty dictionary.
2. Iterate through array `arr`. For each unique appearance of a value add `+1` to the key.
3. Create a list of all the values in the dictionary.
4. Finally check whether they are unique or not using this code
```Python3
return len(set(values)) == len(values)
```
# Space and time complexity
The time complexity is O(n) and the space complexity is O(u), where n is the length of the input list and u is the number of unique elements in the input list.
