# Variable parameters

def sum(*summands):
    print(len(summands), "Numbers")
    print(summands)

    erg = 0
    for s in summands:
        erg += s
    print("Sum:", erg)
    print(type((summands)))

# Aufrufe
sum(3, 4)
sum(3, 8, 12, -5)

