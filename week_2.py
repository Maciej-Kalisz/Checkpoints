import random
from scipy import stats


def random_ints() -> list[int]:
    nums: list[int] = []

    for i in range(10):
        nums.append(random.randint(1, 100))

    return nums


def random_evens() -> list[int]:
    nums: list[int] = []

    while len(nums) < 10:
        if (x := random.randint(1, 100)) % 2 == 0:
            nums.append(x)

    return nums


def random_floats() -> list[float]:
    nums: list[float] = []

    for i in range(10):
        nums.append(round(random.random(), 3))

    return nums


def check_random():
    sample: list[int] = []
    counts: list[int] = []
    count_dict = {}

    for _ in range(1000):
        sample.append(random.randint(1, 10))

    for i in range(1, 10 + 1):
        counts.append(sample.count(i))
        count_dict[i] = sample.count(i)

    indiv_ps: list[float] = []

    for x in counts:
        indiv_ps.append(((x - 100) * (x - 100)) / 100)

    chi_square = sum(indiv_ps)

    print(f"The chi-square value was {chi_square}")

    for k, v in count_dict.items():
        print(f"Count of {k}: {v}")

    p_value = 1 - stats.chi2.cdf(chi_square, 9)
    print(f"The p-value was {p_value}")

    if p_value <= 0.05:
        print("Python is truly random")
    else:
        print("Python is not truly random")

# print(random_ints())
# print(random_evens())
# print(random_floats())
check_random()