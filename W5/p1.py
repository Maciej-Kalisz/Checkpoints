def perfect_square(n):
    for i in range(0, n + 1):
        if i*i == n:
            return True

    return False


def perfect_cube(n):
    for i in range(0, n + 1):
        if i*i*i == n:
            return True

    return False