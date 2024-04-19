def isAnagram(s: str, t: str) -> bool:
    """
    Description:
        This function checks if two sentences are anagrams

    Argss:
        s: string
        t:string

    Return:
        True: if both words are anagraams
        False: if they are not
    """
    s_dict = {}
    t_dict = {}

    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1

    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1

    return t_dict == s_dict


print("Example 1")
s = "anagram"
t = "nagaram"
print(f"Is {s} an anagram of {t}? {isAnagram(s,t)}")

print("Example 2")
s = "rat"
t = "car"
print(f"Is {s} an anagram of {t}? {isAnagram(s,t)}")