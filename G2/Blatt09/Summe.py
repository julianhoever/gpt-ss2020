def userSum():
    zahl = int(input("Ganzzahl eingeben, Eingabe 0 beendet das Programm: "))
    
    if zahl == 0:
        return 0
    else:
        return zahl + userSum()
