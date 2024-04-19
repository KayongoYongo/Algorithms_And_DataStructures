def removeStars(s: str) -> str:
    stars = []

    for char in s:
        if char == "*":
            stars and stars.pop()
        else:
            stars.append(char)

    return "".join(stars)

s = "leet**cod*e"
print(f"The original string is {s}")
print(f"The modified string is {removeStars(s)}")