print("Dieses Programm berechnet die Summe der eingegebenen Zahlen. Eingabe 0 beendetdas Programm.")

summe = 0

zahl = float(input("Bitte geben Sie eine Kommazahl ein:"))

while zahl != 0:
    summe += zahl
    zahl = float(input("Bitte geben Sie eine Kommazahl ein:"))

print("Summe:", summe)

