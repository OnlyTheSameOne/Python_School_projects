"""
Autor:          Same Djafari
Beschreibung:   °F zu °C
Version:        1.0
Datum:          19.09.24
"""
# Input vom User in eine Variable abspeichern
fahrenheit = float(input("Geben sie ihre Temperatur (°F) an: "))

# Berechnung von °F zu °C
celsius = (fahrenheit - 32) * (5/9)

# runden der Zahl um eine nach komma stelle
rund_celsius = round(celsius, 1)

# Ausgabe der brechnung der Temperatur
print("Es sind: " + str(rund_celsius) + "°C")