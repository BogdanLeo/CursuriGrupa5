meniu = {
    "1" : "Afisare lista de cumparaturi",
    "2" : "Adaugare element",
    "3" : "Stergere element",
    "4" : "Stergere lista de cumparaturi",
    "5" : "Cautare in lista de cumparaturi"
}

element = input("Introdu un numar din meniu: ")

if element in meniu:
    print(meniu[element])
else:
    print(f"{element} nu a fost gasit")
 #   if element == 1:
 #      print(value)
 #   elif element == 2:
 #          print(value)
 #   elif element == 3:
 #           print(value)
 #    elif element == 4:
 #           print(value)
 #  elif element == 5:
 #          print(value)
 #   else:
#       print("Valoarea nu exista")