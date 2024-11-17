"""
Autor:          Same Djafari
Beschreibung:   Lösung für die Aufgabe 2
Version:        1.0
Datum:          19.09.24
"""
#Schreibe ein Programm was eine zahl x und folgendes berechnet

# Mathematik biblothek 
import math

# x mit pi multiplizieren

x = int(input("Geben sie eine Zahl ein "))


ergebnis = x * math.pi

# print(ergebnis)10

rund_ergebnis = round(ergebnis, 2)

print("Ihr Ergebnis " + str(rund_ergebnis))

#Eine Zahl y hoch 3

y = int(input("Gib mal eine Zahl "))

x = pow(3, 3)
pergebnis = y * x

print("Ihr gebnis hoch 3 ist: " + str(pergebnis))
 
#Wurzel aus z


z = int(input("Wurzel aus: "))

zergebnis = math.sqrt(z)

print("Die wurzel aus " + str(z) + " ist: " + str(zergebnis))