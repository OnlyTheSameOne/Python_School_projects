"""
Autor:          Same Djafari
Beschreibung:   Lösung für die Aufgabe 6
Version:        1.0
Datum:          19.09.24
"""
#ganze zahlen ein liest und schaut ob sie durch zwei teilbar sind Modulo %
zahl = int(input("Gib mir eine ganze Zahl: "))

#berechnung 
ergebnis = zahl % 2

# wiederholungen = zahl // 2

#abfrage und output als überprüfung
if ergebnis ==  0:
    print("Ja deine Zahl ist grade")
else: 
    print("Nein deine Zahl ist ungrade")
  

#print(ergebnis)