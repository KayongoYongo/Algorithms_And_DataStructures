#!/usr/bin/python3

def romanToInt(s: str) -> int:
    """
    This function converts a string from roman
    to an integer. This is under the assumption
    that the provided string is a valid
    Roman number

    Args:
        s: This is a string representation of the roman number

    Return:
        An integer representation of the roman number
    """
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # This value stores the value of the total
    total = 0
    
    # Stores the value of the previous value
    prev_value = 0

    # Iterate through the string
    for symbol in s:
        # Check the value against the dictionary
        value = roman_values[symbol]
        # If the value is greater than the previous one
        if value > prev_value:
            # If it is true, subtract the value twice
            total += value - 2 * prev_value
        else:
            total += value
        # Reassign pre_value
        prev_value = value

    return total

print("Example 1")
s = "III"
print("The integer representation of {} is {}.".format(s, romanToInt(s)))
print("Example 2")
s = "LVIII"
print("The integer representation of {} is {}.".format(s, romanToInt(s)))
print("Example 3")
s = "MCMXCIV"
print("The integer representation of {} is {}.".format(s, romanToInt(s)))
