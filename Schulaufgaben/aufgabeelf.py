"""
Autor:          Same Djafari
Beschreibung:   Brutto Produkt rechner
Version:        1.0
Datum:          01.10.24
"""
#Der Nutzer gibt seine Geldbetarg an: Dieser wir in a abgespeichert
produktpreis = float(input("Gib ein Produktpreis ein für welches du den bruttopreis habe willst: "))

#Der Nutzer wird nach dem MwSt satz gefargt zur auswahl stehn 19% oder 7% (1 oder 2) Int: ist hier wichtig
kategorie = int(input("Wenn dein Produkt mit (19%) besteuert wird dann drücke eine 1 bei (7%) die 2: "))

#Die Bediengung wird vergliechen mit der Antowrt des Nutzers 
if kategorie == 1:

    produktpreis = produktpreis / 1.19

    #Runden auf 2 komma
    produktpreis = round(produktpreis, 2)

    print("Dein Bruttopreis beträgt: " + str(produktpreis) + "€")

elif kategorie == 2:

    produktpreis = produktpreis / 1.07

    #Runden auf 2 komma
    produktpreis = round(produktpreis, 2)

    print("Dein Bruttopreis beträgt: " + str(produktpreis) + "€")

#Abfangen der falschen eingaben bei der Kategorie wahlen
elif kategorie > 2 or kategorie < 2:
    print("Du hast eine falsche eingabe bei der Kategroie wahl !")


#Aufgabenstellung
"""
Schreiben sie ein Pogramm,
welches den Nettopreis und die MwSt-Kategorie für ein Produkt einließ.
(Kategorie 1 = 7% : Kategorie 2 = 19%) Das Programm soll im Anschluss den Bruttopreis
für das Produkt ausgebne. 
"""