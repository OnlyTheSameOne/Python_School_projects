"""
Autor:          Same Djafari
Beschreibung:   Ohmisches Gestz
Version:        1.0
Datum:          19.09.24
"""
# defeniere variablen und fragt den user nach den werten zum berechnen
u =  float(input("Gibt deine Spannung (Volt) ohne einheit an: "))
r =  float(input("Gib deine Wiedertand (ohm) ein:  "))

#fromel zur berrechnung (ohmisches gesetz umgefomrt)
i = u/r

#runden des ergebnis auf 2 komma stellen
rund_i = round(i, 2)

# ausgabe des ergebnis im Terminal
print("Ihr Strom ist: " + str(rund_i) + " Amper")
