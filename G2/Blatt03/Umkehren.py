a = list(range(3, 31, 3))

l = len(a) - 1

while l >= len(a)//2:
    x = a[l]
    a[l] = a[len(a)-l-1]
    a[len(a)-l-1] = x
    l -= 1

for z in a:
    print(z)

