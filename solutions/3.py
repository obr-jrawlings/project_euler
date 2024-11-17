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


a = primefactors(600851475143)
ans = max(a)
print(ans)
