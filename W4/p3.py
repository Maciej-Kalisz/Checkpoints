# Even

# for i in range(0, 20, 2):
#     print(i)

# Odd

# for i in range(1, 20, 2):
#     print(i)

# For average

n = int(input("Enter an integer: "))

running_sum = 0

for i in range(0, n + 1):
    running_sum = running_sum + i

if not n == 0:
    print(f"The average is {running_sum / (n + 1)}")
else:
    print("The average is 0.0")