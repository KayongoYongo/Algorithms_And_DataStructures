## Leetcode Problem: 1768. Merge Strings Alternately

You are given two strings `word1` and `word2.` Merge the strings by adding letters in **alternating order**, starting with **word1**. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the ***merged string***


# The problem
**This question requires us to merge strings alternatively. This is quite straight forward. Using this example:**

***Input: word1 = "abc", word2 = "pqr"***
***Output: "apbqcr"***

# Things to consider:
Varous challenges arise from this question. They are:
* Iterate through both strings at the same time.
* Access each string such that if the last character is reached, there would not be an index error

# Solution
1. Initialize an empty string to store the merged letters.
2. Find the length of both strings.
3. Using the inbuilt python function **max**, compare the two integers and pick the highest value.
4. The max value will be used to iterate though the strings avoiding access to characters that do not exist.
5. During the process of iteration, if the index i is less than the length of any word, append the letter to the merged string.
6. Return the merged word.
eg 
``` Python
# Roughly
merged = ""
max = len(word1), len(word2)
for i in range(max):
	if i < len(word1):
		merged += word1[i]
	if i < len(word2):
		merged += word2[i]

return merged
```
