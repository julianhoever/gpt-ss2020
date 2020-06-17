a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))

teilbar = b % a == 0 or a % b == 0

print(teilbar)
