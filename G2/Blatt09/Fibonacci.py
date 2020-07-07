def fib(n):
    # Basisfall
    if n <= 2:
        return 1
    # Rekursiver Aufruf
    else:
        return fib(n-2) + fib(n-1)
