a = float(input("Enter a base: "))
n = int(input("Enter an exponent: "))

an = 1

if n >= 0:
    for i in range(1, n+1):
        an = an * a
else:
    n = -n
    for i in range(1, n+1):
        an = an * a

    an = 1/an

print(f"The power is {an}")