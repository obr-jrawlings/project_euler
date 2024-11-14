import math

#  Solution
n = 100000
ans = 0
for x in range(1, n):
    if (x % 3 == 0) or (x % 5 == 0):
        ans += x
print(ans)


# Alternate

def DivisibleBy(target, n):
    p = math.floor(target / n)
    return n * (p * (p + 1)) * 1 / 2


n = 99999
ans = (DivisibleBy(n, 3) + DivisibleBy(n, 5)) - DivisibleBy(n, 15)

print(ans)
