#  Project Euler.net  Problem 864
# Let C(n) be the number of squarefree integers of the form x^2 + 1 such that 1 <= x <= n
# For example, C(10) = 9 and C(1000) = 895
# Find C(123567101113)


def PrimeFactors(value):
    i = 2
    factors = []
    while i * i <= value:
        if value % i:
            i += 1
        else:
            value //= i
            if i not in factors:
                factors.append(i)
            else:
                return None
    if value > 1:
        if value not in factors:
            factors.append(value)
        else:
            return None

    return factors


n = 123567101113
count = 0
for x in range(1, n+1):
    y = x * x + 1
    if PrimeFactors(y) is not None:
        count += 1
        print(count)

