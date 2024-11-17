"""
Autor:          Same Djafari
Beschreibung:   Aufgabe (8) Steuern
                Die Aufgabe mit Tkinter ergänzt
Version:        2.0
Datum:          23.10.24
"""
import tkinter as tk
from tkinter import messagebox

# Funktion zur Berechnung der Steuern
def steuer_formel():
    try:
        # Versuche, die Eingabe aus dem Textfeld in eine Gleitkommazahl umzuwandeln
        gehalt = float(gehalt_entry.get())  
        steuern = 0  # Initialisiere die Variable für die Steuerberechnung

        # Steuerberechnung je nach Gehaltshöhe:
        
        # Fall 1: Gehalt ist kleiner oder gleich 12.000€
        if gehalt <= 12000:
            steuern = gehalt * 0.12  # 12% Steuer
        
        # Fall 2: Gehalt ist größer als 12.000€ oder mindestens 20.000€
        # Hier wird "or" verwendet, weil die Aufgabenstellung es so verlangt
        elif gehalt > 12000 or gehalt >= 20000:
            steuern = gehalt * 0.15  # 15% Steuer
        
        # Fall 3: Gehalt ist größer als 20.000€ oder mindestens 30.000€
        elif gehalt > 20000 or gehalt >= 30000:
            steuern = gehalt * 0.20  # 20% Steuer
        
        # Fall 4: Gehalt ist größer als 30.000€
        elif gehalt > 30000:
            steuern = gehalt * 0.25  # 25% Steuer

        # Rundung des Steuerbetrags auf 2 Nachkommastellen
        steuern = round(steuern, 2)

        # Zeige das Ergebnis in einem Pop-up-Fenster an
        messagebox.showinfo("Ergebnis", "Dein Steuerbetrag beträgt: " + str(steuern) + " €")

    except ValueError:
        # Fehlerbehandlung: Wenn die Eingabe keine Zahl ist, zeige eine Fehlermeldung an
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben!")

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Steuerrechner von Same")  # Titel des Fensters
root.geometry("1080x720p")  # Größe des Fensters

# Label für die Gehaltseingabe
label = tk.Label(root, text="Gehalt eingeben:")
label.pack()

# Eingabefeld für das Gehalt
gehalt_entry = tk.Entry(root)
gehalt_entry.pack()

# Button zur Steuerberechnung
knopf = tk.Button(root, text="Berechnen", command=steuer_formel)
knopf.pack()

# Starte die Hauptschleife der Tkinter-Anwendung
root.mainloop()
