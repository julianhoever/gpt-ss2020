a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

teilbar = (a % b == 0) or (b % a == 0)

print(teilbar)
