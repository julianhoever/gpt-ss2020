n1 = input("Name 1: ")
n2 = input("Name 2: ")
n3 = input("Name 3: ")

if n1 < n2 and n1 < n3:
    print(n1)
    if n2 < n3:
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
elif n2 < n1 and n2 < n3:
    print(n2)
    if n1 < n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
else:
    print(n3)
    if n1 < n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)

