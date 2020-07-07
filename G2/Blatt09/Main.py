import sys
from Fibonacci import fib
from Summe import userSum

if len(sys.argv) > 1:
    zahl = int(sys.argv[1])
    print(fib(zahl))
else:
    print("Summe =", userSum())
