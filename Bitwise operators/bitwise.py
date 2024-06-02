n1 = 7
n2 = 4

print(bin(n1)[2:])
print(bin(n2)[2:])

# AND
# For AND, 1 AND == 1. Everything else is zero
n3 = n1 & n2
# print(bin(n3)[2:])

# OR
# For OR, 0 and 0 is zero. Everythin else is 1
n4 = n1 | n2
# print(bin(n4)[2:])

# XOR
# If the two value are different, we will get a 1. Otherwise, a zero
# if 1 XOR 1, result is 0. 
n5 = n1 ^ n2
# print("0" + bin(n5)[2:])

# NOT 

# SHIFTS
number = 20
print(number)
print(bin(number)[2:])
number <<= 1
print(number)
print(bin(number)[2:])
number >>= 2
print(number)
print(bin(number)[2:])