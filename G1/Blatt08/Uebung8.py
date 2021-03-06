import sys
import Palindrom
import Quersumme
#from Palindrom import palindrom
#from Quersumme import quersumme


try:
    zahl = int(sys.argv[1])
    
    print("Quersumme:", Quersumme.quersumme(zahl))
    
except ValueError:
    wort = sys.argv[1]
    
    if Palindrom.palindrom(wort):
        print(wort, "ist ein Palindrom.")
    else:
        print(wort, "ist kein Palindrom.")
    
except IndexError:
    print("Kein Programmparameter übergeben.")
