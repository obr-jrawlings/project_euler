from collections import Counter

def primefactors(val):
    i = 2
    factors = []
    while i * i <= val:
        if val % i:
            i += 1
        else:
            val //= i
            factors.append(i)
    if val > 1:
        factors.append(val)

    return factors


n = 20
list_dicts = []
for x in range(1, n + 1):
    a = primefactors(x)
    list_dicts.append(Counter(a))

result_dict = {}
for counter in list_dicts:
    for key, value in counter.items():
        result_dict[key] = max(result_dict.get(key, 0), value)
ans = 1
for base, exponent in result_dict.items():
    ans *= base ** exponent

print(ans)
