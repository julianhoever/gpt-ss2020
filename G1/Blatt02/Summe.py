print("Dieses Programm berechnet die Summe der eingegebenen Zahlen. Eingabe 0 beendetdas Programm.")

summe = 0

a = float(input("Bitte geben Sie eine Kommazahl ein: "))

while a != 0:
    summe += a
    a = float(input("Bitte geben Sie eine Kommazahl ein: "))

print("Summe:", summe)
