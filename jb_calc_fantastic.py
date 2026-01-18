
import tkinter as tk

def ajouter(val):
    entree.insert(tk.END, val)

def effacer():
    entree.delete(0, tk.END)

def effacer_un():
    texte = entree.get()
    entree.delete(0, tk.END)
    entree.insert(0, texte[:-1])

def calculer():
    try:
        formule = entree.get().replace("×", "*").replace("÷", "/")
        resultat = str(eval(formule))
        entree.delete(0, tk.END)
        entree.insert(0, resultat)
    except:
        entree.delete(0, tk.END)
        entree.insert(0, "Erreur")

# Fenêtre principale
fen = tk.Tk()
fen.title("Calculatrice simple")
fen.geometry("300x380")
fen.resizable(False, False)

# Champ de texte
entree = tk.Entry(fen, font=("Arial", 18), justify="right")
entree.pack(fill="x", padx=10, pady=10)

# Boutons
boutons = [
    ("7","8","9","÷"),
    ("4","5","6","×"),
    ("1","2","3","-"),
    ("0",".","=", "+")
]

# Grille des boutons
cadre = tk.Frame(fen)
cadre.pack()

for ligne in boutons:
    row = tk.Frame(cadre)
    row.pack(fill="x")
    for b in ligne:
        if b == "=":
            btn = tk.Button(row, text=b, font=("Arial", 16), width=5, height=2,
                            command=calculer, bg="#4CAF50", fg="white")
        else:
            btn = tk.Button(row, text=b, font=("Arial", 16), width=5, height=2,
                            command=lambda val=b: ajouter(val))
        btn.pack(side="left", padx=3, pady=3)

# Ligne des actions spéciales
actions = tk.Frame(fen)
actions.pack(pady=5)

tk.Button(actions, text="C", font=("Arial", 16), width=6, height=2,
          command=effacer, bg="#f44336", fg="white").pack(side="left", padx=5)

tk.Button(actions, text="⌫", font=("Arial", 16), width=6, height=2,
          command=effacer_un).pack(side="left", padx=5)

fen.mainloop()
