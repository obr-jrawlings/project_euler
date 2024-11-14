x = 1
val = 0
_list = [1, 2]

while val < 4000000:
    _list.append(_list[x - 1] + _list[x])
    x += 1
    val = _list[x - 1] + _list[x]

ans = 0
for y in _list:
    if y % 2 == 0:
        ans += y

print(ans)
