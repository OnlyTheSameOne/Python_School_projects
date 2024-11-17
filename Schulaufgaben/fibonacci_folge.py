"""
Autor:          Same Djafari
Beschreibung:   Fibonacci-Folge
Version:        1.0
Datum:          29.10.24
"""

"""
Wikipedia Text:
Die Fibonacci-Folge ist die unendliche Folge natürlicher Zahlen,
die mit zweimal der Zahl 1 beginnt und,
bei der jede Zahl die Summe der beiden ihr vorangehenden Zahlen ist. 
In moderner Schreibweise wird diese Folge zusätzlich mit einer führenden Zahl 0 versehen.
"""
# Anwender wird nach die länge der ausgabe gefragt
N = int(input("Gib die Zahl ein bis welcher ich die Fibonacci-Folge ausgegeben werden soll: "))
# a und b werden als die ersten beiden zahlen intialisiert
a = 0
b = 1
# num ist der schleifenzähler
num = 0

while num < N:
    print(a)  # Ausgabe von a (aktuelles Fibonacci-Folge)
    print()   # Lerzeichen für die Fomartierung
    sum = a + b  # nächstes fibonacci Zahl berechnen und in summe abspeichern
    a = b         # a speichert den wert von b ab
    b = sum      # b wird die neue Fibonacci Zahl 
    num += 1      # Die anzahl der Dürchläufe hochzählen
