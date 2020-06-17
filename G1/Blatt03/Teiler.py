zahl = int(input("Geben Sie eine Zahl ein: "))

for i in range(1, zahl+1):
    if zahl % i == 0:
        print(i)

