"""
Autor:          Same Djafari
Beschreibung:   Absolutbwert von X
Version:        1.0
Datum:          24.09.24
"""
# eine zahl als eingabe vom User
x = int(input("Gib die Zahl ein desen Absokutwert du haben willst "))

# if abfrage die überprüft ob die zahl positiv oder negative ist
if x <= 0:
#vorzeichen positv zu negativ
      absolutwert = -x
else:
#vorziechne negativ zu positv
      absolutwert = x
      

print(absolutwert)