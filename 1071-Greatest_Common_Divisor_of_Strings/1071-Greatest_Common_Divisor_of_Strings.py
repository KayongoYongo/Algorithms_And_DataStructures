def gcdOfStrings(str1: str, str2: str) -> str:
    l1, l2 = len(str1), len(str2)

    for i in range(l1, 0, -1):
        # find the factors
        if l1 % i != 0:
            continue
        
        # finds the sub strings
        sub = str1[:i]

        # copies
        copies = l1 // i

        # check if copies
        if sub * copies != str1:
            continue

        # copies
        copies = l2 // i

        # check if copies
        if sub * copies != str2:
            continue

        return sub

    return ""

str1 ="ABCABC"
str2 ="ABC"
print(f"For {str1} and {str2}, the gcd of sub strings is {gcdOfStrings(str1, str2)}")