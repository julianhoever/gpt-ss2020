import sys
from Summe import userSum
from Fibonacci import fib

if len(sys.argv) > 1:
    zahl = int(sys.argv[1])
    print(fib(zahl))
else:
    print("Summe =", userSum())
