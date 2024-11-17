"""
Autor:          Same Djafari
Beschreibung:   °F zu °C
Version:        1.0
Datum:          19.09.24
"""
import math

r1 = float(input("Gebe deinen ersten wert in r1 an: "))
r2 = float(input("Gebe deinen zweiten wet in r2 an: "))

A =  ((r2*r2* math.pi) - (r1*r1*math.pi))
rund_a = round(A, 2)

print("Die fläche deines Kreisrings beträgt:" + str(rund_a))