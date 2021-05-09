nume = input("Enter your name: ")
val = input("Enter your value: ")
text = f"Sirul de numere a fost gasit de {nume}"

if type(val) == int:
    print(text)
else:
    text = f"Sirul de caractere a fost gasit de {nume}"
    print(text)
