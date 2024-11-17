"""
Autor:          Same Djafari
Beschreibung:   Aufgabe 9 N Zaheln ausgebn
Version:        1.0
Datum:          24.09.24
"""

    # N ist die Zahl die der User eingibt 
N = int(input("Gib deine Zahl an bis zu welchen wert du alle narütlichen Zahlen haben willst: "))

# Zahl bestimmt die wie oft das programm durchlaufen soll
zahl = 0

# while-schleife wenn zahl kleiner N(eingabe des user) ist dann addiere 1 und gib die zahl aus 
# ergibt solange eine Zahl aus bis Zahl nicht mehr kleiner N ist 
while zahl < N:
    zahl = zahl + 1
    print(zahl)
    print()







   