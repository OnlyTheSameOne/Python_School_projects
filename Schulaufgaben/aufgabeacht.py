"""
Autor:          Same Djafari
Beschreibung:   Aufgbae (8) Steueren
Version:        1.0
Datum:          26.09.24
Version:        2.0
Datum:          01.10.24
"""

#Abfarge nach dem Gehalt desen Stuere berechnet werden soll
gehalt = float(input("Wie hoch ist dein Gehalt? "))
steuern = 0

#If abfragen um das Gehalt in die richitge Steuersatklasse zuordnen und berchenn des Stuerebertags7
#bis einschl. 12.000€
if gehalt <= 12000:
    #12%
    steuern = gehalt * 0.12

#von 12.000€ bis einschl. 20.000€
elif gehalt > 12000 or gehalt >= 20000:
    #15%
    steuern = gehalt * 0.15
#von 20.000€ bis einschl. 30.000€
elif gehalt > 20000 or gehalt >= 30000:
    #20%
    steuern = gehalt * 0.20 
#über 30.000€ 
elif gehalt > 30000:
    #25%
    steuern = gehalt * 0.25

#Stuerebetrag auf 2 komma runnden
steuern = round(steuern, 2)

#Ausgabe des ergebnis
print("Dein Steuerbetrag beträgt: " + str(steuern) + "€" )

"""
if gehalt > 30000:
   steuern = gehalt * 0.25
elif gehalt <= 30000:
    steuern = gehalt * 0.2
elif gehalt <= 20000:
    steuern = gehalt * 0.15
elif gehalt <= 12000:
   steuern = gehalt * 0.12
else:
    print(str(gehalt)) 
    
round(steuern, 1)
print("Deine Steuern bertagen: " + str(steuern) + " €")
"""

