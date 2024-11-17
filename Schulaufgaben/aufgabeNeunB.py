"""
Autor:          Same Djafari
Beschreibung:   Aufgabe 9 N Zaheln summe
Version:        1.0
Datum:          24.09.24
"""
# Anwender gibt eine zahl die summiert werden soll
n = int(input("Gib eine Zahl an bis der die Zahlen summiert werden sollen: "))
# Summe und Zahl werden als variablen mit den werten 0, 1 initialisiert

summe = 0
# Zahl ist der Schleifenzähler und zählt die durchläufe
zahl = 1

while zahl <= n:
    summe = summe + zahl
    zahl = zahl + 1
print("Die Summe beträgt:",summe)


