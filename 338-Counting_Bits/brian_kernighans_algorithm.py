def countBits(n):
    count = 0

    while (n != 0):
        n = n & (n-1)
        count += 1

    return count

n = 9

print(f"The number of 1 bits in {n} are {countBits(n)}")