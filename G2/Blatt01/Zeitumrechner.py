import sys

seconds = int(sys.argv[1])

s = seconds % 60
m = seconds // 60 % 60
h = seconds // 60 // 60 % 24
d = seconds // 60 // 60 // 24 % 365
y = seconds // 60 // 60 // 24 // 365

print(seconds, "Sekunden sind", y, "Jahr(e),", d, "Tag(e),", h, "Stunde(n),", m, "Minute(n) und", s, "Sekunde(n).")

# seconds = 500 Sekunden
# s = 500 % 60        = 20 Sekunden
# m = 500 // 60 % 60  = 8 Minuten
# h = 500 // 60 // 60 = 0 Stunden
