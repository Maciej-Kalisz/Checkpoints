def factorial(x):
    fact = 1
    for i in range(1, x + 1):
       fact = fact * i
    return fact

def power(x, y):
    accum = 1
    for i in range(0, y):
        accum *= x

    return accum

n = 5
k = 3

n_fact = factorial(n)
k_fact = factorial(k)
n_minus_k_fact = factorial(n - k)

n_choose_k = n_fact / (k_fact * n_minus_k_fact)

p = power((1/6), k)
q = power((5/6), n-k)

prob = n_choose_k * p * q
print("probability of throwing 3 sixes with 5 dice is", prob)