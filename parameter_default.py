# Funktion
def volumen(width, length, depth=1, color="black"):
    print("Values:", width, length, depth, color)
    erg = width * length * depth
    print("Volumes:", erg, "Farbe:", color)

# Aufrufe
volumen(4, 6, 2, "red")
volumen(2, 12, 7)
volumen(5, 8)
volumen(4, 7, color="red")
