nombre1 = input("Entrez le premier nombre: ")
nombre2 = input("Entrez le second nombre: ")
if not (nombre1.isnumeric() and nombre2.isnumeric()):
    raise SystemExit("Fin du programme, entrez un nombre entier.")
nombre1 = int(nombre1) 
nombre2 = int(nombre2)
operation = input("Entrez le symbole de votre operation: ")
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
