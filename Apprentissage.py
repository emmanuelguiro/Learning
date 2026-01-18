nombre1 = input("Entrez le premier nombre ! ")
nombre2 = input("Entrez le second nombre ! ")
if not (nombre1.isnumeric() and nombre2.isnumeric()):
    raise SystemExit("Fin du programme, entrez un nombre entier.")
nombre1 = int(nombre1) 
nombre2 = int(nombre2)
operation = input("Entrez le symbole de votre operation! ")
if operation not in ["+","-","*","/"] and operation == "/" and nombre2 == "0":
    raise SystemExit("Cette operation est impossible")
if operation == "+" :
    resultats = nombre1 + nombre2
elif operation == "-" :
    resultats = nombre1 - nombre2
elif operation == "*" : 
    resultats = nombre1 * nombre2
else :
    resultats = nombre1 / nombre2
    resultats = round(resultats, 3)
    print(f"Le resultat est : {nombre1},{operation},{nombre2} ={resultats}")


# Quand tu as des erreurs et tu ne sais d'où ça vient
# si le code n'est pas beaucoup
# tu peu metre eb commentaire et aller etape par etape pour voir où ça coince.

# mais dans ton cas c'est deja claire:
#  File "C:\Learning\Apprentissage.py", line 3 : il te donne 
#  le nom du fichier qui pause pb et il te donne la ligne qui pause pb

# if not (nombre1.isnumeric() and nombre2.is.numeric())
# il te précise que dans cette ligne c'est le "is" qui pause pb

# donc corrige!
# fait moi signe par whasapp si le message d'erreur change
#  quand tu auras fini de corriger ce pb