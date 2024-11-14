ans = []

for x in range(100, 999):
    for y in range(100, 999):
        num = x * y
        temp = num
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
        if temp == rev:
            ans.append(temp)

ans = max(ans)

print(ans)
