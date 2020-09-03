# Funktion
def volumes(width, length, depth, color):
    print("Werte:", width, length, depth, color)
    erg = width * length * depth
    print("Volumen:", erg, "Farbe:", color)

# Aufrufe
volumes(4, 6, 2, "red")
volumes(length=2, color="yellow", depth=7, width=3)
volumes(5, depth=2, length=8, color="blue")

# Error
# volumes(3, depth=4, length=5, "black")
