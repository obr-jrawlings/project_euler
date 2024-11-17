#Solution

n = 100
i = 0
j = 0

for x in range(1, n+1):
    i += x**2
a = i

for x in range(1, n+1):
    j += x
b = j**2

ans = (b-a)
print(ans)

#  Alternate for large numbers!
sums = (n*(n + 1))/2
sum_sq = ((2*n + 1)*(n + 1)*n)/6
print((sums*sums)-sum_sq)

