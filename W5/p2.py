def reverse(x: int):
    digits = [int(d) for d in str(x)]
    new = []

    for i in range(len(digits) - 1, -1, -1):
        new.append(digits[i])

    return int(str(new).replace("[", "").replace("]", "").replace(", ", ""))

def palindrome(x: int):
    if reverse(x) == x:
        return True
    else:
        return False